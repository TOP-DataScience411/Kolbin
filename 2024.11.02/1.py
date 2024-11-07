from sys import stdin

sum, cnt = 0, 0
for num in stdin:
    cnt += 1
    try:
        if float(num) > 0:
            sum += float(num)
    except ValueError:
        cnt -= 1
        print("Вводите только числа!")
    if cnt == 3:
        break

print(sum)


# C:\My\Учеба\Kolbin\Kolbin\2024.11.02
  # 9:02:12 > python 1.py
# 13.1
# 65
# -23
# 78.1