num = int(input())

digit_3 = num % 10
num = num // 10
digit_2 = num % 10
num = num // 10
digit_1 = num

print(f"Сумма цифр = {digit_1 + digit_2 + digit_3}")
print(f"Произведение цифр = {digit_1 * digit_2 * digit_3}")



# C:\My\Учеба\Kolbin
 # 18:02:18 > python 4.py
# 333
# Сумма цифр = 9
# Произведение цифр = 27