from sys import stdin, stdout

num, sum = 0, 0
for n in stdin:
    num = int(n)
    break
    
for i in range(int(num / 2)):
    if num % (i + 1) == 0:
        sum += (i + 1)

sum += num
stdout.write(str(sum))


# C:\My\Учеба\Kolbin\Kolbin\2024.11.03
 # 13:50:56 > python 3.py
# 50
# 93