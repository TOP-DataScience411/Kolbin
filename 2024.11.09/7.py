from sys import stdin, stdout
import ref7

dict_out = {}
for i in ref7.list_of_dicts:
    for key, val in i.items():
        if key not in dict_out:
            dict_out[key] = {val, }
        else:
            dict_out[key].add(val)
        
cnt = 0
for key, value in dict_out.items():
    stdout.write(str(key) + ": " + str(value))
    cnt += 1
    if cnt < len(dict_out):
        stdout.write(",\n")



# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
 # 14:04:40 > python 7.py
# Владивосток: {5},
# Воронеж: {1, 4},
# Екатеринбург: {1, 3, 5},
# Иркутск: {9, 2, 5},
# Москва: {3, 4, 6},
# Новокузнецк: {2, 4},
# Оренбург: {1},
# Саратов: {2},
# Уфа: {9},
# Ярославль: {8, 7},
# Волгоград: {5},
# Нижний Новгород: {8, 2, 5},
# Ростов-на-Дону: {6},
# Тольятти: {1},
# Тюмень: {3},
# Казань: {4},
# Новосибирск: {7},
# Пермь: {3},
# Челябинск: {3},
# Санкт-Петербург: {7}