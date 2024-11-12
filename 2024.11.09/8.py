from sys import stdin, stdout

files_str = ""
for names in stdin:
    files_str = names[:-1]
    break
    
files_list = files_str.split("; ")
files_list.sort()

files_out = []
for i in range(len(files_list)):
    cnt = 1
    temp_name = files_list[i]
    temp = temp_name
    for j in range(len(files_out)):
        if temp == files_out[j]:
            cnt += 1
            temp = f"{temp_name.split(".", maxsplit=1)[0]}_{cnt}.{temp_name.split(".", maxsplit=1)[1]}"

    files_out.append(temp)
        
for name in files_out:
    stdout.write(name + "\n")
    
    
    
# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
 # 15:38:30 > python 8.py
# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# aux.h
# functions.h
# main.cpp
# main_2.cpp
# main_3.cpp
# src.tar.gz
# src_2.tar.gz