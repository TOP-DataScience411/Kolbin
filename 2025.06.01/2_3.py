from matplotlib import pyplot as plt
from numpy import corrcoef
from pandas import DataFrame, Series, read_csv
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf

from pathlib import Path
from sys import path


dir_path = Path(path[0])
merged_df = read_csv(dir_path / 'Coins_sort.csv', index_col="Дата", parse_dates=True)

# Определение периода рассмотрения
period_start = "2016-06-01"
period_end = "2025-06-03"
merged_df = merged_df[period_start:period_end]
merged_df = merged_df.resample("ME").mean()  # D W M Y QS

colors = ['#7277fe',  '#6c92f0',  '#66ade1',  '#5fc9d3',  '#59e4c5',  '#acf2e2',  '#d6f9f1']
datas_len = int(len(merged_df)/4)
shifts = range(1, datas_len)


fig = plt.figure(figsize=(12, 8))
axs = fig.subplots(2, 2)
for s, color in zip(shifts, colors):
    axs[0, 0].plot(merged_df["Цена Bitcoin"].shift(s), c=color)
    axs[0, 1].plot(merged_df["Цена Ethereum"].shift(s), c=color)
axs[0, 0].set_title("Bitcoin shifts")
axs[0, 1].set_title("Ethereum shifts")


btc_coeffs = []
eth_coeffs = []
for shift in shifts:
    btc_corr = corrcoef(merged_df["Цена Bitcoin"][:-shift], merged_df["Цена Bitcoin"][shift:])[0, 1]
    btc_coeffs.append(btc_corr)
    eth_corr = corrcoef(merged_df["Цена Ethereum"][:-shift], merged_df["Цена Ethereum"][shift:])[0, 1]
    eth_coeffs.append(eth_corr)

axs[1, 0].scatter(shifts, btc_coeffs)
axs[1, 0].set_title("Bitcoin avtocorrelation")
axs[1, 1].scatter(shifts, eth_coeffs)
axs[1, 1].set_title("Ethereum avtocorrelation")
plt.show()


plot_acf(merged_df["Цена Bitcoin"], lags=datas_len, title="Bitcoin avtocorrelation")  
plot_acf(merged_df["Цена Ethereum"], lags=datas_len, title="Ethereum avtocorrelation")  
plt.show()