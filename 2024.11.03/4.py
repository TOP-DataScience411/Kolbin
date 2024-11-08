from sys import stdin, stdout

n, quantity = 0, 0
for num in stdin:
    n = int(num)
    break
    
left_border = int("1" + "0" * (n - 1))
right_border = int("1" + "0" * n)
for i in range(left_border, right_border):
    cnt = 1 if i != 1 else 0
    for j in range(2, int(i / 2 + 1)):
        if i % j == 0:
            cnt = 0
            break
    quantity += cnt
            
stdout.write(str(quantity))



# C:\My\Учеба\Kolbin\Kolbin\2024.11.03
 # 15:15:37 > python 4.py
# 3
# 143

# C:\My\Учеба\Kolbin\Kolbin\2024.11.03
 # 15:16:32 > python 4.py
# 2
# 21