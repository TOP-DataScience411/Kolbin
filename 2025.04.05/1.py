from pandas import read_csv, DataFrame, Series
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from pathlib import Path
from sys import path


dir_path = Path(path[0])
data_path = dir_path / 'boston.csv'

data = read_csv(data_path, comment='#')

# Матрицы корреляций
corr_matrix_pearson = data.corr('pearson').round(2)
corr_matrix_spearman = data.corr('spearman').round(2)

# Отбраковка выбросов
data_out = data.loc[data['MEDV'] != data['MEDV'].max()]


# Отбракованные зависимые переменные и целевая переменная
X = data_out.loc[:, ['CRIM', 'INDUS', 'RM', 'AGE', 'LSTAT']]
Y = data_out['MEDV']
# Неотбракованные зависимые переменные и целевая переменная
X_raw = data.loc[:, 'CRIM':'LSTAT']
Y_raw = data['MEDV']


# Разбиение обработанных данных с помощью библиотеки scikit-learn
x_train, x_test, y_train, y_test = train_test_split(
    X, Y,
    test_size=0.2,    # Соотношение разбиения
    random_state=17,  # Определяет псевдослучайное разбиение, необходимо менять
)

# Разбиение необработанных данных с помощью библиотеки scikit-learn
x_train_raw, x_test_raw, y_train_raw, y_test_raw = train_test_split(
    X_raw, Y_raw,
    test_size=0.2,    # Соотношение разбиения
    random_state=17,  # Определяет псевдослучайное разбиение, необходимо менять
)


# создание моделей
model = LinearRegression()
model_raw = LinearRegression()

# обучение моделей
model.fit(x_train, y_train)
model_raw.fit(x_train_raw, y_train_raw)

# вычисление предсказанных значений для тестовой выборки
y_pred = model.predict(x_test)
y_pred_raw = model_raw.predict(x_test_raw)
# оценка эффективности с помощью метрик R-квадрат и среднеквадратичная ошибка
R2 = r2_score(y_test, y_pred)   # от 0 до 1. 0 - плохо. Нормированное значение
R2_raw = r2_score(y_test_raw, y_pred_raw)   # от 0 до 1. 0 - плохо. Нормированное значение
# RMSE - СКО, MSE - дисперсия
RMSE = (sum((y_test - y_pred)**2) / y_test.shape[0])**.5    # 0 - хорошо. В единицах измерения целевой переменной
RMSE_raw = (sum((y_test_raw - y_pred_raw)**2) / y_test_raw.shape[0])**.5    # 0 - хорошо. В единицах измерения целевой переменной

print(f'Для обработанных данных:\nR2 = {R2:.3f}\nRMSE = {RMSE:.1f}\n')
print(f'Для необработанных данных:\nR2 = {R2_raw:.3f}\nRMSE = {RMSE_raw:.1f}')



# C:\My\Учеба\Kolbin\Kolbin\2025.04.05
#  10:14:16 > python 1.py
# Для обработанных данных:
# R2 = 0.782
# RMSE = 3.2
# 
# Для необработанных данных:
# R2 = 0.700
# RMSE = 4.5