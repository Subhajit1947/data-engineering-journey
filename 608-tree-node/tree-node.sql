# Write your MySQL query statement below

select
id,
case 
    when p_id is NULL then 'Root' else
    (case 
        when id in (select p_id from Tree where p_id is not NULL) then 'Inner' else 'Leaf' 
        end
    ) 
end as type

from Tree


