from sys import stdin, stdout

fructs = []
for fr in stdin:
    fr = fr.strip()
    if len(fr) > 0:
        fructs.append(fr)
    else:
        break
        
str_out = fructs[0]
for i in range(1, len(fructs)):
    if len(fructs) == i + 1:
        str_out += " и " + fructs[i]
    else:
        str_out += ", " + fructs[i]

stdout.write(str_out)



# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
  # 9:39:10 > python 2.py
# яблоко

# яблоко

# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
  # 9:39:35 > python 2.py
# яблоко
# груша

# яблоко и груша

# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
  # 9:39:45 > python 2.py
# яблоко
# груша
# апельсин

# яблоко, груша и апельсин

# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
  # 9:40:19 > python 2.py
# яблоко
# груша
# апельсин
# лимон

# яблоко, груша, апельсин и лимон