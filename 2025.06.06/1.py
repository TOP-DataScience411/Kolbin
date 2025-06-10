from pandas import read_csv
from numpy import log1p, diff, inf
from matplotlib import pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import itertools

from sys import path
from pathlib import Path

path_dir = Path(path[0])
births = read_csv(path_dir / "births.csv", index_col = "date", parse_dates=True)
births = births.resample("D").mean()

print(adfuller(births)[1], "Ряд стационарный" if adfuller(births)[1] < 0.05 else "Ряд нестационарный")
if adfuller(births)[1] > 0.05:
    births = log1p(births)
    print(adfuller(births)[1], "Ряд стационарный" if adfuller(births)[1] < 0.05 else "Ряд нестационарный")
if adfuller(births)[1] > 0.05:
    births = diff(births.values.flatten())
    print(adfuller(births)[1], "Ряд стационарный" if adfuller(births)[1] < 0.05 else "Ряд нестационарный")
# Сезонность необходимо определять в зависимости от результатов изменения частоты измерений.


# # Подбор гиперпараметров
# p = d = q = range(0, 5)
# pdq = list(itertools.product(p, d, q))  # Все комбинации (p,d,q)
# best_bic = inf
# for params in pdq:
#     model_A = ARIMA(births, order=params)
#     model_A_res = model_A.fit(method='statespace')
#     model_S = SARIMAX(births, order=params, enforce_stationarity=True)
#     model_S_res = model_S.fit(method='powell', maxiter=500, disp=True)
#     if model_A_res.bic < best_bic:
#         best_params_A = params
#     if model_S_res.bic < best_bic:
#         best_params_S = params
# print("Оптимальные значения p, d, q для ARIMA:", best_params_A)
# print("Оптимальные значения p, d, q для SARIMAX:", best_params_S)



model_A = ARIMA(births, order=(4, 3, 4))    
model_A_res = model_A.fit()

model_S = SARIMAX(births, order=(4, 4, 4), enforce_stationarity=True)
model_S_res = model_S.fit(method='powell', maxiter=500, disp=True)

end_pred = len(births) + 2
pred_A = model_A_res.predict(end=end_pred)
pred_S = model_S_res.predict(end=end_pred)



fig, axs = plt.subplots(2, 1, figsize=(14, 8))
axs[0].plot(births)
axs[0].plot(pred_A)
axs[0].set_title("ARIMA")
axs[1].plot(births)
axs[1].plot(pred_S)
axs[1].set_title("SARIMAX")
plt.show()