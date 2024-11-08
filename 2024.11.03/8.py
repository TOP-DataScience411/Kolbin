from sys import stdin, stdout

n = 0
sequence = []
for num in stdin:
    n = int(num)
    break
    
for i in range(n):
    if i > 1:
        sequence.append(sequence[i-1] + sequence[i-2])
    else:
        sequence.append(1)

for elem in sequence:
    stdout.write(str(elem) + " ")



# C:\My\Учеба\Kolbin\Kolbin\2024.11.03
 # 13:43:01 > python 8.py
# 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597