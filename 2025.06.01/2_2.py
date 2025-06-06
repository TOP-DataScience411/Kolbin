from matplotlib import pyplot as plt
from pandas import DataFrame, Series, read_csv
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

from pathlib import Path
from sys import path


dir_path = Path(path[0])
merged_df = read_csv(dir_path / 'Coins_sort.csv', index_col="Дата", parse_dates=True)

# Определение периода рассмотрения
period_start = "2016-01-01"
period_end = "2025-06-03"
merged_df = merged_df[period_start:period_end]


# Изменение шага взятия стоимости (для присвоения свойства frec индексу датафрейма)
merged_df = merged_df.resample("ME").mean()  # D W M Y QS



# Декомпозиция "вручную"
window = 6
components = ['observed', 'trend', 'seasonal', 'resid']
# Нахождение скользящего среднего
merged_df_ma = merged_df.rolling(window).mean()  # D W M Y QS

btc_season = merged_df["Цена Bitcoin"] - merged_df_ma["Цена Bitcoin"].shift(-window)
eth_season = merged_df["Цена Ethereum"] - merged_df_ma["Цена Ethereum"].shift(-window)
for i in range(len(merged_df - window)):
    btc_subgroup = btc_season[i::window]
    btc_season.iloc[i] = btc_subgroup.mean()
    eth_subgroup = eth_season[i::window]
    eth_season.iloc[i] = eth_subgroup.mean()
    
btc_resid = merged_df["Цена Bitcoin"] - merged_df_ma["Цена Bitcoin"].shift(-window) - btc_season
eth_resid = merged_df["Цена Ethereum"] - merged_df_ma["Цена Ethereum"].shift(-window) - eth_season

fig, axs = plt.subplots(4, 2, figsize=(16, 8))
axs[0, 0].plot(merged_df["Цена Bitcoin"])
axs[1, 0].plot(merged_df_ma["Цена Bitcoin"])
axs[2, 0].plot(btc_season)
axs[3, 0].plot(btc_resid)

axs[0, 1].plot(merged_df["Цена Ethereum"])
axs[1, 1].plot(merged_df_ma["Цена Ethereum"])
axs[2, 1].plot(eth_season)
axs[3, 1].plot(eth_resid)

for i, comp in enumerate(components):
    axs[i, 0].set_title(f'Bitcoin {comp}')
    axs[i, 1].set_title(f'Ethereum {comp}')



# # Декомпозиция при помощи seasonal_decompose из пакета statsmodels.tsa.seasonal
# btc_decompose = seasonal_decompose(merged_df[f"Цена Bitcoin"], period=window)
# eth_decompose = seasonal_decompose(merged_df[f"Цена Ethereum"], period=window)
# 
# fig, axes = plt.subplots(4, 2, figsize=(16, 8))
# 
# components = ['observed', 'trend', 'seasonal', 'resid']
# for i, comp in enumerate(components):
#     btc_decompose_comp = getattr(btc_decompose, comp)
#     eth_decompose_comp = getattr(eth_decompose, comp)
#     
#     axes[i, 0].plot(btc_decompose_comp)
#     axes[i, 0].set_title(f'Bitcoin {comp}')
#     
#     axes[i, 1].plot(eth_decompose_comp)
#     axes[i, 1].set_title(f'Ethereum {comp}')



bitcoin_stational = adfuller(merged_df[f"Цена Bitcoin"])
ethereum_stational = adfuller(merged_df[f"Цена Ethereum"])
print(f"Bitcoin: {'стационарный' if bitcoin_stational[1] > 0.05 else 'нестационарный'}")
print(f"Ethereum: {'стационарный' if ethereum_stational[1] > 0.05 else 'нестационарный'}")

plt.tight_layout()
plt.show()
