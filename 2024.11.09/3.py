from sys import stdin, stdout

nums_str = []
cnt = 0
for seq in stdin:
    nums_str.append(seq)
    cnt += 1
    if cnt == 2:
        break
    
nums_1 = nums_str[0].split()    
nums_2 = nums_str[1].split()

# Вариант с циклами
# for i in range(len(nums_1)):
    # if nums_1[i] == nums_2[0]:
        # for j in range(1, len(nums_2)):
            # if nums_1[i+j] != nums_2[j]:
                # stdout.write("нет")
                # break
            # if j == len(nums_2)-1:
                # stdout.write("да")
        # break
    # elif i == len(nums_1) - 1:
        # break

# Вариант со срезами
if nums_2[0] in nums_1:
    index = [i for i in range(len(nums_1)) if nums_1[i] == nums_2[0]]
    index = index[0]
    if nums_2 == nums_1[index: (index+len(nums_2))]:
        stdout.write("да")
    else:
        stdout.write("нет")



# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
 # 10:31:01 > python 3.py
# 1 2 3 4
# 1 2
# да

# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
 # 10:32:38 > python 3.py
# 1 2 3 4
# 2 4
# нет