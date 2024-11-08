from sys import stdin, stdout

n, sum = 0, 0
for num in stdin:
    n = int(num)
    break

for num in stdin:
    if int(num) > 0:
        sum += int(num)
    n -= 1
    if n == 0:
        break

stdout.write(str(sum))


# C:\My\Учеба\Kolbin\Kolbin\2024.11.03
 # 13:41:26 > python 2.py
# 6
# 3
# -5
# 1
# 10
# -1
# 8
# 22