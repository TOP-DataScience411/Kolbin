from sys import stdin, stdout

email = ""
for str in stdin:
    email = str
    break
    
if email.count("@") == 1 and email.count(".") == 1:
    if email.find("@") + 2 < email.find("."):
        stdout.write("да")
    else:
        stdout.write("нет")
else:
    stdout.write("нет")
    
    
    
# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
  # 9:22:33 > python 1.py
# sgd@ya.ru
# да

# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
  # 9:22:38 > python 1.py
# abcde@fghij
# нет