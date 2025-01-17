-- 1. Вывести названия всех стран Евразии
select 
    Name 
from 
    country 
where 
    Continent=1 or 
    Continent=2;
   
   
-- 2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет 
select 
    Region, 
    Name 
from 
    country 
where 
    LifeExpectancy < 50;
    
    
-- 3. Вывести название самой крупной по площади страны Африки
select 
    Name 
from 
    country 
where 
    SurfaceArea=(
        select 
            max(SurfaceArea) 
        from 
            country 
        where 
            Continent=4
        );
    
-- Второй вариант запроса    
select 
    Name 
from 
    country 
where 
    Continent=4 
order by 
    SurfaceArea desc 
limit 
    1;
    
    
-- 4. Вывести названия пяти азиатских стран с самой низкой плотностью населения
select 
    Name 
from 
    country 
where 
    Continent=1 
order by 
    (SurfaceArea / Population) desc 
limit 
    5;
    
    
-- 5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять миллионов человек
select 
    CountryCode, 
    Name 
from 
    city 
where 
    Population > 5000000 
order by 
    Population;
    
    
-- 6. Вывести название города в Индии с самым длинным названием для подсчёта количества символов используйте встроенную функцию char_length()
select 
    Name 
from 
    city 
where 
    CHAR_LENGTH(Name)=(
        select 
            max(CHAR_LENGTH(Name)) 
        from 
            city 
        where 
            CountryCode="IND"
        ) 
and 
    CountryCode="IND";