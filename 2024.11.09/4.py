from sys import stdin, stdout

errors_dict = {}
for er in stdin:
    er = er.strip().split()
    if len(er) > 0:
        errors_dict[er[0]] = er[1]
    else:
        break

value = ""
for v in stdin:
    value = v[:-1]
    break

key_out = None
for key, val in errors_dict.items():
    if val == value:
        stdout.write(key)
        key_out = key

if not key_out:
    stdout.write("! value error !")
    
    
    
# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
 # 11:45:19 > python 4.py
# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB
# 1007 ER_DB_CREATE_EXISTS

# ER_CANT_CREATE_DB
# 1006

# C:\My\Учеба\Kolbin\Kolbin\2024.11.09
 # 11:46:29 > python 4.py
# 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# 4108 ER_GIPK_COLUMN_EXISTS

# ER_CANT_OPEN_FILE
# ! value error !