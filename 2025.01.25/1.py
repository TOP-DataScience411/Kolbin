from re import compile, MULTILINE
from sys import path
from pathlib import Path

months = (
    'января', 'январь',
    'февраля', 'февраль',
    'марта', 'март',
    'апреля', 'апрель',
    'мая', 'май',
    'июня', 'июнь',
    'июля', 'июль',
    'августа', 'август',
    'сентября', 'сентябрь',
    'октября', 'октябрь',
    'ноября', 'ноябрь',
    'декабря', 'декабрь'
)
           
day_pattern = r"(?:[1-9]|0[1-9]|[12]\d|3[01])"
month_pattern = f"(?:{'|'.join(months)})"
year_pattern = r"\d\d\d\d г\."

pattern = (f"^{day_pattern} {month_pattern} {year_pattern}|" 
           f"^{day_pattern} {month_pattern} {year_pattern} – {day_pattern} {month_pattern} {year_pattern}|" 
           f"^{day_pattern}–{day_pattern} {month_pattern} {year_pattern}|"
           f"^{day_pattern} {month_pattern} – {day_pattern} {month_pattern} {year_pattern}|"
           f"^{month_pattern}–{month_pattern} {year_pattern}|"
           f"^{month_pattern} {year_pattern}|"
           f"^{year_pattern}|"
           r"^(?:\d\d\d\d–\d\d\d\d гг\.)"
           )
           
prog = compile(pattern, MULTILINE)
text = (Path(path[0]) / "history_dates_ed.txt").read_text("utf-8")

result = prog.findall(text)
print(result)