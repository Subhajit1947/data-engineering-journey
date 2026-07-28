select
person_name 
from
(
select 
    *,
    SUM(weight) OVER (ORDER BY turn) as cumulative_weight
from Queue
) q
where cumulative_weight<=1000
order by cumulative_weight desc limit 1