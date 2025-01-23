-- 1. Вывести названия стран и названия сопоставленных им столиц
select 
    country.Name, 
    city.Name 
from 
    country 
join 
    city on Capital = ID;
    
-- 2. Сравнить по регионам сумму населения стран и сумму населения городов
select 
    c.Region, 
    sum(c.Population) as "Население стран", 
    sum(city.Population) "Население городов" 
from 
    country as c 
join 
    city on Code=CountryCode 
group by 
    c.Region;
    
-- 3. Вывести десять языков, на которых разговаривает больше всего людей
select 
    Language, 
    round(sum(Population*Percentage/100)) as Native_speakers 
from 
    country 
join 
    countrylanguage on Code = CountryCode 
group by 
    Language 
order by 
    Native_speakers desc 
limit 10;

-- 4. Вывести названия специальностей и суммарное количество дней отпусков, в которых были врачи каждой специальности; отсортировать по возрастанию суммарного количества дней отпуска
select 
    spec.name, 
    coalesce(sum(end_date - start_date), 0) as sum_vacations 
from 
    specializations as spec 
    left join doctors_specs as d_spec on spec.id = spec_id
    left join doctors as d on d.id = d_spec.doctor_id
    left join vacations as v on v.doctor_id = d.id
group by 
    spec.name
order by 
    sum_vacations;
    
-- 5. Вывести округлённую до целого сумму средств, которую можно выделить на одну палату этого отделения (в зависимости от количества палат в отделении), от всех пожертвований каждому отделению; отсортировать по убыванию найденной суммы
select 
    depart as department, 
    sum(amount) as total_amount,
    quantity_wards,
    round(sum(amount) / quantity_wards) as amount_per_ward
from 
    donations as d
join 
    (select 
        dep.id as d_id, 
        dep.name as depart, 
        count(*) as quantity_wards
    from 
        departments as dep
    join 
        wards as w on w.dep_id = dep.id
    group by 
        d_id) as subq on subq.d_id = d.dep_id
group by 
    depart, 
    quantity_wards
order by 
    amount_per_ward;