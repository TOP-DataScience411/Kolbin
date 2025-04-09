from pandas import DataFrame, read_csv
from sys import path
from pathlib import Path
import math 
from numpy import array, full, corrcoef, zeros
from matplotlib import pyplot as plt


dir_path = Path(path[0])
path_science_investetions = dir_path / "science_investetions.csv"
path_early_malignancy = dir_path / "early_malignancy.csv"

data_science_investetions = array(read_csv(path_science_investetions, comment="#"))
data_early_malignancy = array(read_csv(path_early_malignancy, comment="#"))


# Получение списка всех годов
years = set([data[0].split()[0] for data in data_science_investetions])
for y in data_early_malignancy:
    years.add(y[0].split()[0])
years = sorted(list(years))


# Создание полной таблицы данных
var_series = full((3, len(years)), None)
# var_series = zeros((3, len(years)), dtype=float)
for i in range(len(var_series[1])):
    var_series[0][i] = int(years[i])
    
    for si in data_science_investetions:
        si = si[0].split()
        if si[0] == years[i]:
            var_series[1][i] = float(si[1])
            break
            
    for em in data_early_malignancy:
        em = em[0].split()
        if em[0] == years[i]:
            var_series[2][i] = float(em[1])
            break
            

SI_min = min([num for num in var_series[1, :] if num])
SI_max = max([num for num in var_series[1, :] if num])
EM_min = min([num for num in var_series[2, :] if num])
EM_max = max([num for num in var_series[2, :] if num])

# Нормализация
norm_series = var_series.copy()
for i in range(len(norm_series[1])):
    if norm_series[1][i]:
        norm_series[1][i] = round((norm_series[1][i] - SI_min) / (SI_max - SI_min), 2)
    if norm_series[2][i]:
        norm_series[2][i] = round((norm_series[2][i] - EM_min) / (EM_max - EM_min), 2)
     
norm_series_table = DataFrame(norm_series[1:, :], index=["science_investetions", "early_malignancy"], columns=norm_series[0, :])


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
    return round(x.corr(y), 3), x, y
    
# Определение всех вариантов смещения. -2 для обеспечения достаточного количества наблюдений
max_shift = norm_series_table.shape[1]-2
shifts = range(-max_shift, max_shift)
results = []

for shift in shifts:
    corr, x, y = calculate_shifted_corr(
            norm_series_table.loc["science_investetions"], 
            norm_series_table.loc["early_malignancy"], 
            shift)
    if not math.isnan(corr):
        results.append((corr, shift, x, y))
        print(f"Сдвиг: {shift} лет")
        print(f"Ряд 1:\n{x}") 
        print(f"Ряд 2:\n{y}") 
        print(f"Корреляция: {corr}\n")
# Предупреждения выводятся из-за недостатка данных при передаче значений None

best_corr, best_shift, x, y = max(results)

print(f"\nЛучшее смещение: {best_shift}, \nЗначение корреляции {best_corr}.\n")

# Это здесь для наглядности данных
# all_data = array([
        # [2007, 352917701.2,  None],
        # [2008, 410864983.6,  None],
        # [2009, 461006216.0,  None],
        # [2010, 489450798.7,  None],
        # [2011, 568386749.7,  None],
        # [2012, 655061743.4,  None],
        # [2013, 699948879.0,  50.8],
        # [2014, 795407850.6,  52.0],
        # [2015, 854288043.8,  53.7],
        # [2016, 873778705.8,  54.7],
        # [2017, 950257084.9,  55.6],
        # [2018, 960689437.2,  56.4],
        # [2019, 1060560377.0, 57.4],
        # [2020, 1091333468.1, 56.3],
        # [2021, 1193578508.5, 57.9],
        # [2022, 1322563915.0, 59.3],
        # [2023, None,         60.5],
    # ])

# fig = plt.figure()
# axs = fig.subplots()

# axs.plot(x, y)
# fig.show()