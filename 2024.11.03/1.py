from sys import stdin, stdout

nums = []
for num in stdin:
    if int(num) % 7 == 0:
        nums.append(num[0:-1])
    else:
        break

for i in range(len(nums), 0, -1):
    stdout.write(nums[i-1] + " ")
    
    
# C:\My\Учеба\Kolbin\Kolbin\2024.11.03
 # 13:32:30 > python 1.py
# 7
# 14
# 21
# 2
# 21 14 7