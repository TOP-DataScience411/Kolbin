from sys import path
from pathlib import Path
    
def list_files(path):
    cwd = Path(path)
    for _, _, files in cwd.walk():
        return tuple(files)

# Второй вариант реализации
# def list_files(path):
    # cwd = Path(path)
    # out = []
    # for p in cwd.iterdir():
        # out.append(p.name)
    # return tuple(out)
    
    
path = r"C:\My\Учеба\Kolbin\Kolbin\2024.12.14"

# >>> path
# 'C:\\My\\Учеба\\Kolbin\\Kolbin\\2024.12.14'
# >>> list_files(path)
# ('# HW 2024.12.14.txt', '1.py', '2.py', '3.py', '4.py', '5.py')