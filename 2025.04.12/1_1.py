from pandas import Series, DataFrame
from scipy.io.arff import loadarff
from pathlib import Path
from sys import path
# from matplotlib import pyplot as plt, rcParams
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import math


dir_path = Path(path[0])
data_path = dir_path / "dataset_55_hepatitis.arff"

data_raw = DataFrame(loadarff(data_path)[0])

# >>> data_raw["Class"].value_counts()
# Class
# b'LIVE'    123
# b'DIE'      32
# Name: count, dtype: int64


# Разбиение данных на таблицы с зависимыми и целевым параметром
data = data_raw.loc[:, list(data_raw.columns[:-1])]
target = data_raw.loc[:, "Class"].replace({b'DIE': 1, b'LIVE': 0})


# Нормирование данных только для столбцов с числовыми значениями
data_norm = (data.loc[:, data.describe().columns] - data.loc[:, data.describe().columns].describe().loc["mean"]) /data.loc[:, data.describe().columns].describe().loc["std"]

# Замена оставшихся пропусков данных числовых параметров средним значением столбца
for col in data_norm.columns:
    mean = data_norm[col].mean()
    for i in range(data_norm.shape[0]):
        data_norm.loc[i, col] = mean if math.isnan(data_norm[col][i]) else data_norm[col][i]


# Выделение столбцов с категориальными данными в отдельный DataFrame
data_bin = data[['SEX', 'STEROID', 'ANTIVIRALS', 'FATIGUE', 'MALAISE', 'ANOREXIA',
       'LIVER_BIG', 'LIVER_FIRM', 'SPLEEN_PALPABLE', 'SPIDERS', 'ASCITES',
       'VARICES', 'HISTOLOGY']]

# Замена всех нечисловых значений на числовой эквивалент
data_bin_full = data_bin.replace({b"no": 0, b"yes": 1, b"male": 0, b"female": 1, b"?": None}, inplace=False)
    
# Определение строк, содержащих пропуски данных
non_data_indx = set()
for i in range(data_bin.shape[0]):
    if data_bin_full.loc[i].isna().any():
        non_data_indx.add(i)

# Объединение таблиц с числовыми и нечисловыми значениями
data_norm = data_norm.round(2)
all_data = data_norm.join(data_bin_full)

# Удаление 13 строк, содержащих пропуски данных в общей таблице и целевой таблице
all_data.drop(labels=non_data_indx, inplace=True)
target.drop(labels=non_data_indx, inplace=True)

X = all_data
x_train, x_test, y_train, y_test = train_test_split(
    X, target,
    test_size=0.3,
    random_state=1
) 
   
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

conf = confusion_matrix(y_test, y_pred)
TN, FP, FN, TP = conf.ravel()
print("\n\n")
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

''' В результате обучения модель неплохо определяет отсутствие гепатита, но болезнь не определяет вообще, предположительно из-за явного дефицита случаев с симптомами заболевания в наборе данных.'''


# При тестовой выборке 30% от всех данных
# [[33  2]
#  [ 4  4]]
# accuracy = 86.0%
# f1-score = 57.0%
# Вероятность совершить ошибку первого рода = 5.7%
# Вероятность совершить ошибку второго рода = 50.0%

# При тестовой выборке 25% от всех данных
# [[28  2]
#  [ 3  3]]
# accuracy = 86.0%
# f1-score = 55.0%
# Вероятность совершить ошибку первого рода = 6.7%
# Вероятность совершить ошибку второго рода = 50.0%

# При тестовой выборке 20% от всех данных
# [[22  2]
#  [ 3  2]]
# accuracy = 83.0%
# f1-score = 44.0%
# Вероятность совершить ошибку первого рода = 8.3%
# Вероятность совершить ошибку второго рода = 60.0%
