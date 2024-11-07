from sys import stdin

chars = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
nums = ("1", "2", "3", "4", "5", "6", "7", "8")
positions = [[], []]
cnt = 0

while cnt < 2:
    for pos in stdin:
        if len(pos) == 3 and pos[0] in chars and pos[1] in nums:
            positions[cnt].append(chars[pos[0]])
            positions[cnt].append(int(pos[1]))
            cnt += 1
            if cnt == 2:
                break
        else:
            print("Некорректный ввод!")

if positions[0][0] == positions[1][0] or positions[0][1] == positions[1][1]:
    print("да")
else:
    print("нет")
    
    
# C:\My\Учеба\Kolbin\Kolbin\2024.11.02
 # 12:32:19 > python 5.py
# d4
# e4
# да


# C:\My\Учеба\Kolbin\Kolbin\2024.11.02
 # 12:32:33 > python 5.py
# f3
# h1
# нет