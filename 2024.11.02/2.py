from sys import stdin

cnt, divisible, divider = 0, 0, 0
nums = []

while True:
    for num in stdin:
        cnt += 1
        nums.append(num)
        if cnt >= 2:
            break
    try:
        divisible = int(nums[0])
        divider = int(nums[1])
    except ValueError:
        nums.clear()
        cnt = 0
        print("Вводите только целые числа!")
    else:
        break
        
if divisible % divider == 0:
    print(f"{divisible} делится на {divider} нацело\nчастное: {int(divisible / divider)}")
else:
    print(f"{divisible} не делится на {divider} нацело\n"
    f"неполное частное: {divisible // divider}\nостаток: {divisible % divider}")
    
    
# C:\My\Учеба\Kolbin\Kolbin\2024.11.02
  # 9:48:44 > python 2.py
# 8
# 2
# 8 делится на 2 нацело
# частное: 4


# C:\My\Учеба\Kolbin\Kolbin\2024.11.02
  # 9:48:58 > python 2.py
# 10
# 3
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1