from sys import stdin, stdout
import ref5

word = ""
for string in stdin:
    word = string.upper()
    break

scores = 0
for i in range(len(word)):
    for key, val in ref5.scores_letters.items():
        if word[i] in val:
            scores += key
            break
              
stdout.write(str(scores))


# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
 # 12:54:25 > python 5.py
# синхрофазотрон
# 29