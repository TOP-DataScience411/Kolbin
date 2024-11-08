from sys import stdin, stdout

number = 0
for num in stdin:
    number = num
    break
    
sum_1 = int(number[0]) + int(number[1]) + int(number[2])
sum_2 = int(number[3]) + int(number[4]) + int(number[5])
    
if sum_1 == sum_2:
    stdout.write("да")
else:
    stdout.write("нет")
    
    
    
# C:\My\Учеба\Kolbin\Kolbin\2024.11.03
 # 16:09:05 > python 6.py
# 183534
# да

# C:\My\Учеба\Kolbin\Kolbin\2024.11.03
 # 16:16:00 > python 6.py
# 401367
# нет