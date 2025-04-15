from pandas import DataFrame, Series, read_csv
from numpy import array
from sys import path
from pathlib import Path
from datetime import datetime
import locale
from matplotlib import pyplot as plt
import math
from scipy.stats import linregress

datasets_path = Path(path[0])
path_dizel = datasets_path / "dizel_fuel_rus_prices.csv"
path_urals = datasets_path / "urals_oil_rus_export_prices.csv"
locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")

dizel_fuel_price_raw = array(read_csv(path_dizel, header=None))
urals_oil_price_raw = array(read_csv(path_urals, header=None))

# Функция разбивает сырые данные на даты и цены
def data_split(data):
    out_data = []
    for row in data:
        split_row = row[0].split()
        date_row = datetime.strptime(split_row[0], "%d.%b.%y")
        price_row = float(split_row[1])
        out_data.append([date_row.date(), price_row])
    return out_data
    
dizel_fuel_price = data_split(dizel_fuel_price_raw)
urals_oil_price = data_split(urals_oil_price_raw)


def find_corr(data1, data2):
    corr_coef = sum((data1 - diz_mean) * (data2 - oil_mean)) / (sum((data1 - diz_mean)**2)**0.5 * sum((data2 - oil_mean)**2)**0.5)
    return corr_coef
    

# Функция возвращает коэффициент корреляции с заданным сдвигом данных 
def calculate_shifted_corr(data1, data2, shift=0):
    if shift > 0:
        x = data1[:-shift]
        y = data2[shift:]
    elif shift < 0:
        x = data1[abs(shift):]
        y = data2[:shift]
    else:
        x, y = data1, data2
    return round(find_corr(x, y), 3), array(x, dtype=float), array(y, dtype=float)


# Общие данный двух таблиц
all_data = []
for diz in dizel_fuel_price:
    for oil in urals_oil_price:
        if diz[0].year == oil[0].year and diz[0].month == oil[0].month:
            all_data.append([oil[0], diz[1], oil[1]])
all_data = array(all_data).T
print(DataFrame(all_data[1:, :], columns=all_data[0, :]), end="\n\n")


diz_mean = all_data[1, :].mean().round(1)
oil_mean = all_data[2, :].mean().round(1)


# Определение всех вариантов смещения. -1 для обеспечения достаточного количества наблюдений
max_shift = all_data.shape[1] - 1
shifts = range(-max_shift, max_shift)
results = []

for shift in shifts:
    corr, x, y = calculate_shifted_corr(
            all_data[1, :], 
            all_data[2, :], 
            shift)
    if not math.isnan(corr):
        results.append((corr, shift, x, y))
        print(f"Сдвиг: {shift} месяцев")
        print(f"Ряд 1:\n{x}") 
        print(f"Ряд 2:\n{y}") 
        print(f"Корреляция: {corr}\n")

best_corr, best_shift, x, y = max(results)
res = linregress(x, y)
print(f"\nЛучшее значение корреляции {best_corr} при смещении {best_shift} месяцев.")
print(f"Уравнение функции регрессии: y = {res.intercept:.2f} + {res.slope:.2f} * x")


fig = plt.figure()
axs = fig.subplots()
axs.scatter(x, y)
axs.plot(x, res.intercept + res.slope*x, 'r', label='Линия регрессии')
axs.set(xlabel = "dizel fuel", ylabel = "urals oil")
axs.text(
    x.max(), y.min()+20,
    f'Значение корреляции={best_corr}\nСдвиг: {best_shift} месяцев',
    horizontalalignment='right',
    verticalalignment='top'
)
plt.legend()
plt.savefig(datasets_path / "best_corr.png", dpi=300)



# Сдвиг: 59 месяцев
# Ряд 1:
# [34.43 34.16 34.14 34.34]
# Ряд 2:
# [471.2 477.6 419.7 345.1]
# Корреляция: -0.366

# Сдвиг: 60 месяцев
# Ряд 1:
# [34.43 34.16 34.14]
# Ряд 2:
# [477.6 419.7 345.1]
# Корреляция: -0.098

# Сдвиг: 61 месяцев
# Ряд 1:
# [34.43 34.16]
# Ряд 2:
# [419.7 345.1]
# Корреляция: 0.581


# Лучшее значение корреляции 0.76 при смещении -6 месяцев.
# Уравнение функции регрессии: y = -154.84 + 13.77 * x