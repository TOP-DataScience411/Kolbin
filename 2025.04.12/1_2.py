from pandas import Series, DataFrame
from scipy.io.arff import loadarff
from pathlib import Path
from sys import path
from matplotlib import pyplot as plt, rcParams
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


dir_path = Path(path[0])
data_path = dir_path / "dataset_37_diabetes.arff"

data_raw = DataFrame(loadarff(data_path)[0])

# >>> data_raw['class'].value_counts()
# class
# b'tested_negative'  0-  500  - здоров
# b'tested_positive'  1-  268  - диабет


data = data_raw.loc[:, list(data_raw.columns[:-1])]
target = data_raw.loc[:, "class"].replace({b'tested_positive': 1, b'tested_negative': 0})

data_norm = ((data - data.describe().loc["mean"]) / data.describe().loc["std"]).round(2)

X = data_norm
x_train, x_test, y_train, y_test = train_test_split(
    X, target,
    test_size=0.15,
    random_state=1
) 
   
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

conf = confusion_matrix(y_test, y_pred)
TN, FP, FN, TP = conf.ravel()
print(conf)

accuracy = round(((TP + TN) / (TN + FP + FN + TP)), 2)
print(f"accuracy = {accuracy:.1%}")

recall = TP / (TP + FN)
precision = TP / (TP + FP)
specificity = TN / (TN + FP)
f1 = round((2*(recall * precision) / (recall + precision)), 2)
print(f"f1-score = {f1:.1%}")
print(f"Вероятность совершить ошибку первого рода = {(1 - specificity):.1%}")
print(f"Вероятность совершить ошибку второго рода = {(1 - recall):.1%}")

''' Очевидно, недостаточно данных, при этом данные слабо указывают на особенности диабетиков, что видно на графиках.'''

# При тестовой выборке 25% от всех данных
# [[109  14]
#  [ 29  40]]
# accuracy = 78.0%
# f1-score = 65.0%
# Вероятность совершить ошибку первого рода = 11.4%
# Вероятность совершить ошибку второго рода = 42.0%

# При тестовой выборке 20% от всех данных
# [[89 10]
#  [24 31]]
# accuracy = 78.0%
# f1-score = 65.0%
# Вероятность совершить ошибку первого рода = 10.1%
# Вероятность совершить ошибку второго рода = 43.6%

# При тестовой выборке 15% от всех данных
# [[67  8]
#  [16 25]]
# accuracy = 79.0%
# f1-score = 68.0%
# Вероятность совершить ошибку первого рода = 10.7%
# Вероятность совершить ошибку второго рода = 39.0%