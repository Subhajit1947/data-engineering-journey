# Write your MySQL query statement below
with dailyamount as(
    select 
        visited_on,
    sum(amount) as amount
    from Customer 
        group by visited_on    
)

select 
d1.visited_on,sum(d2.amount) as amount,round(avg(d2.amount),2) as average_amount 
from 
    dailyamount d1 
    join 
    dailyamount d2
    on d2.visited_on between date_sub(d1.visited_on,interval 6 day) and d1.visited_on
    group by d1.visited_on
    having count(*)=7





