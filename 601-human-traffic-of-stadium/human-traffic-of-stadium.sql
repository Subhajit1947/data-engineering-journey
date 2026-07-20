with filtered as(
    select *,id-row_number() over(order by id) as isconsecutive
    from Stadium 
    where people>=100
)
select
id,visit_date,people 
from filtered
where isconsecutive in (
    select isconsecutive from filtered group by isconsecutive having count(*)>=3
)
order by visit_date