from datetime import date, timedelta

# vacations = [(date(2023, 5, 1), timedelta(weeks=1)), (date(2023, 7, 17), timedelta(weeks=1))]

def check_weekdays(*days: int) -> list:
    """ Функция проверяет переданные значения на соответствие формату date.isoweekday(). """
    days_out = []
    if any(days):
        for day in days:
            if type(day) is int and 0 < day < 8:
                days_out.append(day)
    return days_out
    
    
def check_vacations() -> list:
    """ Функция проверяет наличие списка vacations в глобальном пространстве имен 
        и в случае его нахождения вычисляет все даты, входящие в его периоды. 
        Возвращает список всех дат vacations. """
    global_vac = globals()
    vacation_val, vacation_periods = [], []
    for key, val in global_vac.items():
        if key == "vacations":
            vacation_val = val
    if not vacation_val:
        return vacation_val
        
    for period in vacation_val:
        for i in range(period[1].days):
            vacation_periods.append(period[0] + timedelta(i))
    return vacation_periods
    

def schedule(
        first_date: date, 
        day_of_week: int, 
        /, 
        *day_nums: tuple, 
        total_days: int, 
        format_str: str = '%d/%m/%Y'
) -> list:
    """ Функция генерирует график проведения мероприятий по заданным условиям.
        Функция принимает дату первого мероприятия в графике, обязательным аргументом один и более номеров дней недели, далее обязательным аргументом общее количество занятий, и необязательным аргументом формат строкового представления генерируемых дат. 
        Функция возвращает список строковых представлений дат в заданном формате. """
    days_of_events = []
    days_of_week = check_weekdays(day_of_week, *day_nums)
    vacation_periods = check_vacations()
    
    cnt = 0
    while True:
        new_date = first_date+timedelta(days=cnt)
        if new_date.isoweekday() in days_of_week and new_date not in vacation_periods:
            days_of_events.append(new_date.strftime(format_str))
        if len(days_of_events) == total_days:
            break
        cnt += 1
    return days_of_events
    
    

# >>> py321 = schedule(date(2023, 4, 1), 6, 7, total_days=70)
# >>> len(py321)
# 70
# >>> py321[28:32]
# ['15/07/2023', '16/07/2023', '29/07/2023', '30/07/2023']