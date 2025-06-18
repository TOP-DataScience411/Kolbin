from pandas import read_csv,  DataFrame, Series
from matplotlib import pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from random import seed, choice

from sys import path
from pathlib import Path

path_dir = Path(path[0])
data_raw = read_csv(path_dir / "boston.csv", comment='#')

# Исключение строк в которых значение целевого параметра максимальное.
data_raw = data_raw.loc[data_raw["MEDV"] != data_raw["MEDV"].max()]

# data_raw_corr = data_raw.corr().round(2)
# fig, axs = plt.subplots(14, 14, figsize=(28, 28))
# for i, col1 in enumerate(data_raw):
    # for j, col2 in enumerate(data_raw):
        # axs[i][j].scatter(data_raw[col1], data_raw[col2], s=7)
        # axs[i][j].text(
            # data_raw[col1].max(), 
            # data_raw[col2].max(),
            # f'p={data_raw_corr.loc[col1, col2]}\n',
            # horizontalalignment='right',
            # verticalalignment='top',
        # )
        # axs[i][j].set(
            # xticks=[], 
            # yticks=[],
            # xlabel=col1,
            # ylabel=col2,
        # )
# fig.savefig(path_dir / 'boston_14x14_graphs.png', dpi=200)


target = data_raw["MEDV"]
# Исключение зависимых параметров с высоким значением корреляции между собой (>=0.7), 
# либо с околонулевой корреляцией с целевым параметром.
data = data_raw.drop(["DIS", "CHAS", "NOX", "TAX", "MEDV"], axis=1)

# Нормирование данных
data_norm = (data-data.mean())/data.std()
data_norm["MEDV"] = target
data_norm.to_csv(path_dir / "boston_filter.csv", index=False)


# data_norm_corr = data.corr().round(2)
# fig, axs = plt.subplots(9, 9, figsize=(28, 28))
# for i, col1 in enumerate(data_norm):
    # for j, col2 in enumerate(data_norm):
        # axs[i][j].scatter(data_norm[col1], data_norm[col2], s=7)
        # axs[i][j].text(
            # data_norm[col1].max(), 
            # data_norm[col2].max(),
            # f'p={data_norm_corr.loc[col1, col2]}\n',
            # horizontalalignment='right',
            # verticalalignment='top',
        # )
        # axs[i][j].set(
            # xticks=[], 
            # yticks=[],
            # xlabel=col1,
            # ylabel=col2,
        # )
# fig.savefig(path_dir / 'boston_filter.png', dpi=200)
