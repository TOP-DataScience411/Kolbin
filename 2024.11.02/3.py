from sys import stdin

year = 0
for num in stdin:
    try:
        year = int(num)
    except ValueError:
        print("Вводите только целые числа!")
    else:
        break

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("да")
else:
    print("нет")
    
    
# C:\My\Учеба\Kolbin\Kolbin\2024.11.02
 # 10:04:42 > python 3.py
# 2000
# да


# C:\My\Учеба\Kolbin\Kolbin\2024.11.02
 # 10:04:51 > python 3.py
# 1000
# нет