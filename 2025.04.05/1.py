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

sum_R2_raw, sum_R2 = 0, 0
sum_RMSE_raw, sum_RMSE = 0, 0
cnt_iter = 20

for i in range(0, cnt_iter):
    # Разбиение обработанных данных с помощью библиотеки scikit-learn
    x_train, x_test, y_train, y_test = train_test_split(
        X, Y,
        test_size=0.2,   
        random_state=i, 
    )

    # Разбиение необработанных данных с помощью библиотеки scikit-learn
    x_train_raw, x_test_raw, y_train_raw, y_test_raw = train_test_split(
        X_raw, Y_raw,
        test_size=0.2,    
        random_state=i,  
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
    # оценка эффективности с помощью метрик R-квадрат и среднеквадратичная ошибка. от 0 до 1. 0 - плохо. 
    R2 = r2_score(y_test, y_pred)   
    R2_raw = r2_score(y_test_raw, y_pred_raw)   
    # RMSE - СКО, MSE - дисперсия. 0 - хорошо. В единицах измерения целевой переменной
    RMSE = (sum((y_test - y_pred)**2) / y_test.shape[0])**.5    
    RMSE_raw = (sum((y_test_raw - y_pred_raw)**2) / y_test_raw.shape[0])**.5    
    
    print(f'Для обработанных данных: R2 = {R2:.3f}; RMSE = {RMSE:.1f}')
    print(f'Для необработанных данных: R2 = {R2_raw:.3f}; RMSE = {RMSE_raw:.1f}\n')
    
    sum_R2_raw += R2_raw 
    sum_R2 += R2
    sum_RMSE_raw += RMSE_raw 
    sum_RMSE += RMSE

print(f'''\nСредние значения метрик при оценке качества моделей, 
обученных на обработанных и необработанных данных для {cnt_iter} итераций:''')
print(f'Для обработанных данных: R2 = {sum_R2/cnt_iter:.3f}; RMSE = {sum_RMSE/cnt_iter:.1f}')
print(f'Для необработанных данных: R2 = {sum_R2_raw/cnt_iter:.3f}; RMSE = {sum_RMSE_raw/cnt_iter:.1f}\n')


# C:\My\Учеба\Kolbin\Kolbin\2025.04.05
#  10:41:01 > python 1.py
# Для обработанных данных: R2 = 0.662; RMSE = 5.1
# Для необработанных данных: R2 = 0.589; RMSE = 5.8
# 
# Для обработанных данных: R2 = 0.674; RMSE = 4.3
# Для необработанных данных: R2 = 0.763; RMSE = 4.8
# 
# Для обработанных данных: R2 = 0.672; RMSE = 4.4
# Для необработанных данных: R2 = 0.779; RMSE = 4.3
# 
# Для обработанных данных: R2 = 0.662; RMSE = 4.9
# Для необработанных данных: R2 = 0.795; RMSE = 4.1
# 
# Для обработанных данных: R2 = 0.700; RMSE = 4.1
# Для необработанных данных: R2 = 0.726; RMSE = 5.0
# 
# Для обработанных данных: R2 = 0.687; RMSE = 4.6
# Для необработанных данных: R2 = 0.733; RMSE = 4.6
# 
# Для обработанных данных: R2 = 0.692; RMSE = 4.1
# Для необработанных данных: R2 = 0.684; RMSE = 5.2
# 
# Для обработанных данных: R2 = 0.707; RMSE = 4.0
# Для необработанных данных: R2 = 0.579; RMSE = 5.8
# 
# Для обработанных данных: R2 = 0.727; RMSE = 4.5
# Для необработанных данных: R2 = 0.708; RMSE = 4.7
# 
# Для обработанных данных: R2 = 0.688; RMSE = 4.8
# Для необработанных данных: R2 = 0.766; RMSE = 4.9
# 
# Для обработанных данных: R2 = 0.673; RMSE = 4.4
# Для необработанных данных: R2 = 0.671; RMSE = 5.9
# 
# Для обработанных данных: R2 = 0.576; RMSE = 5.0
# Для необработанных данных: R2 = 0.686; RMSE = 5.2
# 
# Для обработанных данных: R2 = 0.665; RMSE = 4.2
# Для необработанных данных: R2 = 0.748; RMSE = 4.5
# 
# Для обработанных данных: R2 = 0.601; RMSE = 4.2
# Для необработанных данных: R2 = 0.732; RMSE = 4.9
# 
# Для обработанных данных: R2 = 0.727; RMSE = 4.2
# Для необработанных данных: R2 = 0.618; RMSE = 5.0
# 
# Для обработанных данных: R2 = 0.709; RMSE = 4.6
# Для необработанных данных: R2 = 0.692; RMSE = 4.9
# 
# Для обработанных данных: R2 = 0.697; RMSE = 4.7
# Для необработанных данных: R2 = 0.646; RMSE = 4.8
# 
# Для обработанных данных: R2 = 0.782; RMSE = 3.2
# Для необработанных данных: R2 = 0.700; RMSE = 4.5
# 
# Для обработанных данных: R2 = 0.736; RMSE = 4.5
# Для необработанных данных: R2 = 0.690; RMSE = 5.3
# 
# Для обработанных данных: R2 = 0.661; RMSE = 4.6
# Для необработанных данных: R2 = 0.665; RMSE = 5.9
# 
# 
# Средние значения метрик при оценке качества моделей,
# обученных на обработанных и необработанных данных для 20 итераций:
# Для обработанных данных: R2 = 0.685; RMSE = 4.4
# Для необработанных данных: R2 = 0.699; RMSE = 5.0