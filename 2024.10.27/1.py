from datetime import datetime

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year = input("Введите год рождения: ")

print(surname, name + ",", datetime.now().year - int(year))


# C:\My\Учеба\Kolbin
 # 13:41:26 > python 1.py
# Введите имя: Ivan
# Введите фамилию: Kolbin
# Введите год рождения: 1991
# Kolbin Ivan, 33


# ИТОГ: отлично — 4/4

