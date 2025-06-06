from pandas import DataFrame, Series, read_csv, to_numeric, merge, to_datetime
from pathlib import Path
from sys import path


dir_path = Path(path[0])
data = read_csv(dir_path / 'Bitcoin_daily.csv', index_col="Дата", parse_dates=True)
data_eth = read_csv(dir_path / 'Ethereum_daily.csv', index_col="Дата", parse_dates=True)

data['Цена'] = data['Цена'].str.replace('.', '', regex=False)
data['Цена'] = data['Цена'].str.replace(',', '.', regex=False)
data['Цена'] = to_numeric(data['Цена'], errors='coerce')
data['Откр.'] = data['Откр.'].str.replace('.', '', regex=False)
data['Откр.'] = data['Откр.'].str.replace(',', '.', regex=False)
data['Откр.'] = to_numeric(data['Откр.'], errors='coerce')
data['Макс.'] = data['Макс.'].str.replace('.', '', regex=False)
data['Макс.'] = data['Макс.'].str.replace(',', '.', regex=False)
data['Макс.'] = to_numeric(data['Макс.'], errors='coerce')
data['Мин.'] = data['Мин.'].str.replace('.', '', regex=False)
data['Мин.'] = data['Мин.'].str.replace(',', '.', regex=False)
data['Мин.'] = to_numeric(data['Мин.'], errors='coerce')


data_eth['Цена'] = data_eth['Цена'].str.replace('.', '', regex=False)
data_eth['Цена'] = data_eth['Цена'].str.replace(',', '.', regex=False)
data_eth['Цена'] = to_numeric(data_eth['Цена'], errors='coerce')
data_eth['Откр.'] = data_eth['Откр.'].str.replace('.', '', regex=False)
data_eth['Откр.'] = data_eth['Откр.'].str.replace(',', '.', regex=False)
data_eth['Откр.'] = to_numeric(data_eth['Откр.'], errors='coerce')
data_eth['Макс.'] = data_eth['Макс.'].str.replace('.', '', regex=False)
data_eth['Макс.'] = data_eth['Макс.'].str.replace(',', '.', regex=False)
data_eth['Макс.'] = to_numeric(data_eth['Макс.'], errors='coerce')
data_eth['Мин.'] = data_eth['Мин.'].str.replace('.', '', regex=False)
data_eth['Мин.'] = data_eth['Мин.'].str.replace(',', '.', regex=False)
data_eth['Мин.'] = to_numeric(data_eth['Мин.'], errors='coerce')

data.to_csv(dir_path / "Bitcoin.csv")
data_eth.to_csv(dir_path / "Ethereum.csv")

merged_df = merge(data["Цена"], data_eth["Цена"], on='Дата', suffixes=(" Bitcoin", " Ethereum"), how='inner')
merged_df.index = to_datetime(merged_df.index, dayfirst=True)
merged_df = merged_df.sort_index()
merged_df.to_csv(dir_path / "Coins_sort.csv")

