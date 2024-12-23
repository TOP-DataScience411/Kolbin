from sys import path
from pathlib import Path
from datetime import date
from calendar import monthrange
from typing import Literal
from random import randint
from pprint import pprint


def load_data():
    global names
    male_names, female_names, males_second_names, female_second_names, males_surnames, females_surnames = [], [], [], [], [], []
    work_dir = Path(path[0]) / "data/names"
    
    with open(work_dir / "женские_имена.txt", "r") as output:
        female_names = [line.strip() for line in output.readlines()]
    with open(work_dir / "мужские_имена_отчества.txt", "r") as output:
        male_names_full = output.readlines()
    with open(work_dir / "фамилии.txt", "r") as output:
        surnames_full = output.readlines()
    
    for line in male_names_full:
        line = line.split()
        male_names.append(line[0])
        val = line[1].strip("(")
        males_second_names.append(val.strip(","))
        female_second_names.append(line[2].strip(")"))
        
    for line in surnames_full:
        if len(line.split(", ")) > 1:
            line = line.split(", ")
            for_male = line[0]
            for_female = line[1]
        else:
            for_male = line
            for_female = line
        males_surnames.append(for_male)
        females_surnames.append(for_female[:-1])
        
    names["male_names"] = male_names
    names["female_names"] = female_names
    names["male_second_names"] = males_second_names
    names["female_second_names"] = female_second_names
    names["male_surnames"] = males_surnames
    names["female_surnames"] = females_surnames
    
    
def generate_person():
    out_dict = {
                "имя": str,
                "отчество": str,
                "фамилия": str,
                "пол": Literal['мужской', 'женский'],
                "дата рождения": date,
                'мобильный': str
                }
    
    out_dict["пол"] = "мужской" if randint(0, 1) else "женский"
    
    if out_dict["пол"] == "мужской":
        out_dict["имя"] = names["male_names"][randint(0, len(names["male_names"]) - 1)]
        out_dict["отчество"] = names["male_second_names"][randint(0, len(names["male_second_names"]) - 1)]
        out_dict["фамилия"] = names["male_surnames"][randint(0, len(names["male_surnames"]) - 1)]
    else:
        out_dict["имя"] = names["female_names"][randint(0, len(names["female_names"]) - 1)]
        out_dict["отчество"] = names["female_second_names"][randint(0, len(names["female_second_names"]) - 1)]
        out_dict["фамилия"] = names["female_surnames"][randint(0, len(names["female_surnames"]) - 1)]
    
    year = randint(date.today().year - 100, date.today().year)
    month = randint(1, 12)
    day = randint(1, int(monthrange(year, month)[1]))
    out_dict["дата рождения"] = date(year, month, day)
    
    number = "+79"
    for i in range(9):
        number += str(randint(0, 9))
    out_dict['мобильный'] = number
    
    return out_dict
    
    

names = {}

load_data()
data = generate_person()
pprint(data, sort_dicts=False)


# {'имя': 'Амани',
 # 'отчество': 'Степановна',
 # 'фамилия': 'Полковникова',
 # 'пол': 'женский',
 # 'дата рождения': datetime.date(2024, 11, 5),
 # 'мобильный': '+79154360335'}