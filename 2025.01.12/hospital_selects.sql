-- 1. Вывести средний оклад (salary) всех сотрудников
select 
    round(avg(salary), 2) as mean_salary 
from 
    doctors;

-- 2. Вывести среднюю премию для всех сотрудников, чей доход выше среднего (взять явное значение из результата предыдущего запроса)
select 
    round(avg(salary), 2) as over_mean_salary
from 
    doctors 
where 
    salary > 55641.74;

-- 3. Вывести с сортировкой по возрастанию среднее количество дней в отпуске для каждого сотрудника — в MySQL используйте функцию datediff(), в PostgreSQL используйте вычитание с помощью оператора -
select 
    doctor_id, 
    round(avg(end_date - start_date), 1) as days  
from 
    vacations 
group by 
    doctor_id 
order by 
    days;

-- 4. Вывести для каждого сотрудника самый ранний год отпуска и самый поздний год отпуска с сортировкой по возрастанию разности между этими двумя значениями    
select 
    doctor_id,
    min(extract(year from start_date)) as earliest, 
    max(extract(year from end_date)) as latest 
from 
    vacations 
group by 
    doctor_id 
order by 
    (max(extract(year from end_date)) - min(extract(year from start_date)));
    
-- 5. Вывести сумму пожертвований за всё время для каждого отделения с сортировкой по возрастанию номеров отделений
select 
    dep_id,
    sum(amount) 
from 
    donations 
group by 
    dep_id 
order by 
    dep_id;
    
-- 6. Вывести сумму пожертвований за каждый год для каждого спонсора с сортировкой по возрастанию номеров спонсоров и годов
select 
    sponsor_id, 
    extract(year from date) as year, 
    sum(amount) 
from 
    donations 
group by 
    sponsor_id, 
    extract(year from date) 
order by 
    sponsor_id, 
    extract(year from date);
