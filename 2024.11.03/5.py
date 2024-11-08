from sys import stdin, stdout

chars_cnt = 0
txt = ""
for s in stdin:
    txt = s
    break
    
for i in range(len(txt)):
    if txt[i].isalnum():
        chars_cnt += 1

rub = int(chars_cnt * 0.3)
penny = round((chars_cnt * 0.3 - rub) * 100)
stdout.write(str(rub) + " руб. " + str(penny) + " коп.")


# C:\My\Учеба\Kolbin\Kolbin\2024.11.03
 # 16:08:55 > python 5.py
# грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.