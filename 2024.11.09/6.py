from sys import stdin, stdout

binary_nums = {"b", "0b", "0", "1"}
bin_num = ""
for bin_n in stdin:
    bin_num = bin_n[:-1]
    break
    
result = "да"
for i in range(len(bin_num)):
    if bin_num[i] not in binary_nums or bin_num[0] == "1":
        result = "нет"
        break

stdout.write(result)



# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
 # 13:18:33 > python 6.py
# 0b11001
# да

# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
 # 13:19:23 > python 6.py
# 1b0101
# 0 1
# нет