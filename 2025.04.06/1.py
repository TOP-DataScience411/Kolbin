from matplotlib import pyplot as plt, rcParams
from pandas import DataFrame, Series
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from numpy import fliplr
from pathlib import Path
from sys import path


dir_path = Path(path[0])

data_raw = load_breast_cancer()

data = DataFrame(data_raw['data'], columns=data_raw['feature_names'])
target = Series(data_raw['target'], name='target')

data_all = DataFrame(
      dict(zip(
          data_raw['feature_names'], 
          data_raw['data'].T
      )) 
    | {'target': data_raw['target']}
)


# >>> data.describe().transpose().round(2)
#                          count    mean     std     min     25%     50%      75%      max
# mean radius              569.0   14.13    3.52    6.98   11.70   13.37    15.78    28.11
# mean texture             569.0   19.29    4.30    9.71   16.17   18.84    21.80    39.28
# mean perimeter           569.0   91.97   24.30   43.79   75.17   86.24   104.10   188.50
# mean area                569.0  654.89  351.91  143.50  420.30  551.10   782.70  2501.00
# mean smoothness          569.0    0.10    0.01    0.05    0.09    0.10     0.11     0.16
# mean compactness         569.0    0.10    0.05    0.02    0.06    0.09     0.13     0.35
# mean concavity           569.0    0.09    0.08    0.00    0.03    0.06     0.13     0.43
# mean concave points      569.0    0.05    0.04    0.00    0.02    0.03     0.07     0.20
# mean symmetry            569.0    0.18    0.03    0.11    0.16    0.18     0.20     0.30
# mean fractal dimension   569.0    0.06    0.01    0.05    0.06    0.06     0.07     0.10
# radius error             569.0    0.41    0.28    0.11    0.23    0.32     0.48     2.87
# texture error            569.0    1.22    0.55    0.36    0.83    1.11     1.47     4.88
# perimeter error          569.0    2.87    2.02    0.76    1.61    2.29     3.36    21.98
# area error               569.0   40.34   45.49    6.80   17.85   24.53    45.19   542.20
# smoothness error         569.0    0.01    0.00    0.00    0.01    0.01     0.01     0.03
# compactness error        569.0    0.03    0.02    0.00    0.01    0.02     0.03     0.14
# concavity error          569.0    0.03    0.03    0.00    0.02    0.03     0.04     0.40
# concave points error     569.0    0.01    0.01    0.00    0.01    0.01     0.01     0.05
# symmetry error           569.0    0.02    0.01    0.01    0.02    0.02     0.02     0.08
# fractal dimension error  569.0    0.00    0.00    0.00    0.00    0.00     0.00     0.03
# worst radius             569.0   16.27    4.83    7.93   13.01   14.97    18.79    36.04
# worst texture            569.0   25.68    6.15   12.02   21.08   25.41    29.72    49.54
# worst perimeter          569.0  107.26   33.60   50.41   84.11   97.66   125.40   251.20
# worst area               569.0  880.58  569.36  185.20  515.30  686.50  1084.00  4254.00
# worst smoothness         569.0    0.13    0.02    0.07    0.12    0.13     0.15     0.22
# worst compactness        569.0    0.25    0.16    0.03    0.15    0.21     0.34     1.06
# worst concavity          569.0    0.27    0.21    0.00    0.11    0.23     0.38     1.25
# worst concave points     569.0    0.11    0.07    0.00    0.06    0.10     0.16     0.29
# worst symmetry           569.0    0.29    0.06    0.16    0.25    0.28     0.32     0.66
# worst fractal dimension  569.0    0.08    0.02    0.06    0.07    0.08     0.09     0.21


data_norm = (data - data.describe().loc['mean']) / data.describe().loc['std']


# >>> data_norm.describe().transpose().round(2)
#                          count  mean  std   min   25%   50%   75%    max
# mean radius              569.0  -0.0  1.0 -2.03 -0.69 -0.21  0.47   3.97
# mean texture             569.0   0.0  1.0 -2.23 -0.73 -0.10  0.58   4.65
# mean perimeter           569.0  -0.0  1.0 -1.98 -0.69 -0.24  0.50   3.97
# mean area                569.0  -0.0  1.0 -1.45 -0.67 -0.29  0.36   5.25
# mean smoothness          569.0  -0.0  1.0 -3.11 -0.71 -0.03  0.64   4.77
# mean compactness         569.0   0.0  1.0 -1.61 -0.75 -0.22  0.49   4.56
# mean concavity           569.0   0.0  1.0 -1.11 -0.74 -0.34  0.53   4.24
# mean concave points      569.0  -0.0  1.0 -1.26 -0.74 -0.40  0.65   3.92
# mean symmetry            569.0   0.0  1.0 -2.74 -0.70 -0.07  0.53   4.48
# mean fractal dimension   569.0   0.0  1.0 -1.82 -0.72 -0.18  0.47   4.91
# radius error             569.0   0.0  1.0 -1.06 -0.62 -0.29  0.27   8.90
# texture error            569.0  -0.0  1.0 -1.55 -0.69 -0.20  0.47   6.65
# perimeter error          569.0  -0.0  1.0 -1.04 -0.62 -0.29  0.24   9.45
# area error               569.0  -0.0  1.0 -0.74 -0.49 -0.35  0.11  11.03
# smoothness error         569.0  -0.0  1.0 -1.77 -0.62 -0.22  0.37   8.02
# compactness error        569.0   0.0  1.0 -1.30 -0.69 -0.28  0.39   6.14
# concavity error          569.0   0.0  1.0 -1.06 -0.56 -0.20  0.34  12.06
# concave points error     569.0   0.0  1.0 -1.91 -0.67 -0.14  0.47   6.64
# symmetry error           569.0   0.0  1.0 -1.53 -0.65 -0.22  0.36   7.07
# fractal dimension error  569.0  -0.0  1.0 -1.10 -0.58 -0.23  0.29   9.84
# worst radius             569.0  -0.0  1.0 -1.73 -0.67 -0.27  0.52   4.09
# worst texture            569.0   0.0  1.0 -2.22 -0.75 -0.04  0.66   3.88
# worst perimeter          569.0  -0.0  1.0 -1.69 -0.69 -0.29  0.54   4.28
# worst area               569.0   0.0  1.0 -1.22 -0.64 -0.34  0.36   5.92
# worst smoothness         569.0  -0.0  1.0 -2.68 -0.69 -0.05  0.60   3.95
# worst compactness        569.0  -0.0  1.0 -1.44 -0.68 -0.27  0.54   5.11
# worst concavity          569.0   0.0  1.0 -1.30 -0.76 -0.22  0.53   4.70
# worst concave points     569.0   0.0  1.0 -1.74 -0.76 -0.22  0.71   2.68
# worst symmetry           569.0   0.0  1.0 -2.16 -0.64 -0.13  0.45   6.04
# worst fractal dimension  569.0  -0.0  1.0 -1.60 -0.69 -0.22  0.45   6.84


mean_0 = data_norm.loc[target == 0].mean()
mean_1 = data_norm.loc[target == 1].mean()

groupped = DataFrame({
    'mean 0': mean_0,
    'mean 1': mean_1,
    'diff': abs(mean_0 - mean_1),
}).sort_values(by='diff', ascending=False)


# >>> groupped.round(2)
#                          mean 0  mean 1  diff
# worst concave points       1.03   -0.61  1.64
# worst perimeter            1.02   -0.60  1.62
# mean concave points        1.01   -0.60  1.60
# worst radius               1.01   -0.60  1.60
# mean perimeter             0.96   -0.57  1.53
# worst area                 0.95   -0.56  1.52
# mean radius                0.95   -0.56  1.51
# mean area                  0.92   -0.55  1.47
# mean concavity             0.90   -0.54  1.44
# worst concavity            0.86   -0.51  1.36
# mean compactness           0.77   -0.46  1.23
# worst compactness          0.77   -0.46  1.22
# radius error               0.74   -0.44  1.17
# perimeter error            0.72   -0.43  1.15
# area error                 0.71   -0.42  1.13
# worst texture              0.59   -0.35  0.94
# worst smoothness           0.55   -0.32  0.87
# worst symmetry             0.54   -0.32  0.86
# mean texture               0.54   -0.32  0.86
# concave points error       0.53   -0.31  0.84
# mean smoothness            0.46   -0.28  0.74
# mean symmetry              0.43   -0.25  0.68
# worst fractal dimension    0.42   -0.25  0.67
# compactness error          0.38   -0.23  0.61
# concavity error            0.33   -0.20  0.52
# fractal dimension error    0.10   -0.06  0.16
# smoothness error          -0.09    0.05  0.14
# mean fractal dimension    -0.02    0.01  0.03
# texture error             -0.01    0.01  0.02
# symmetry error            -0.01    0.01  0.01


# Обучение модели на 5 наборах параметров, из списка groupped, взятых по порядку. 
print(f"Результаты оценки модели:\n")
for i in range(0, 30, 6):
    X = data_norm.loc[:, groupped.index[i:i+6]]

    x_train, x_test, y_train, y_test = train_test_split(
        X, target,
        test_size=0.2,
        random_state=1
    )

    model = LogisticRegression()

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    conf_matr = confusion_matrix(abs(y_test - 1), abs(y_pred - 1))
    model_acc = round(1 - sum(fliplr(conf_matr).diagonal()) / sum(conf_matr.diagonal()), 2)
    print(f"при обучении на переменных от {i+1} до {i+6}:\nПроцент точности модели: {model_acc}\n{conf_matr}\n")
    


# Результаты оценки модели:
# 
# при обучении на переменных от 1 до 6:
# Процент точности модели: 0.95
# [[72  0]
#  [ 5 37]]
# 
# при обучении на переменных от 7 до 12:
# Процент точности модели: 0.9
# [[67  5]
#  [ 5 37]]
# 
# при обучении на переменных от 13 до 18:
# Процент точности модели: 0.91
# [[69  3]
#  [ 6 36]]
# 
# при обучении на переменных от 19 до 24:
# Процент точности модели: 0.73
# [[63  9]
#  [15 27]]
# 
# при обучении на переменных от 25 до 30:
# Процент точности модели: 0.52
# [[63  9]
#  [28 14]]

