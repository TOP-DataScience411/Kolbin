from matplotlib import pyplot as plt
from pandas import DataFrame, Series, read_csv
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

from pathlib import Path
from sys import path


dir_path = Path(path[0])
data = read_csv(dir_path / 'births.csv', index_col="Date", parse_dates=True)
print(data)

# # Декомпозиция "вручную"
# window = 10
# # Нахождение скользящего среднего
# data_ma = data.rolling(window).mean()  
# bitcoin_season = data["Births"] - data_ma["Births"].shift(-window)
# for i in range(len(data - window)):
#     subgroup = bitcoin_season[i::window]
#     bitcoin_season.iloc[i] = subgroup.mean()
#     
# residual_fluct = data["Births"] - data_ma["Births"].shift(-window) - bitcoin_season
# 
# fig = plt.figure(figsize=(12, 8))
# axs = fig.subplots(3, 1)
# axs[0].plot(data_ma["Births"])
# axs[0].plot(data["Births"])
# axs[1].plot(bitcoin_season)
# axs[2].plot(residual_fluct)
# plt.show()



# Декомпозиция при помощи seasonal_decompose библиотеки statsmodels.tsa.seasonal
data_decompose = seasonal_decompose(data["Births"])
   
fig = data_decompose.plot()
fig.set_size_inches(9, 12)
# fig = plt.figure(figsize=(12, 8))
# axs = fig.subplots(3, 1)
# axs[0].plot(coin_decompose.observed)
# axs[0].plot(coin_decompose.trend)
# axs[1].plot(coin_decompose.seasonal)
# axs[2].plot(coin_decompose.resid)
plt.show()


data_stational = adfuller(data["Births"])
print(f"Births: {'стационарный' if data_stational[1] > 0.05 else 'нестационарный'}")
