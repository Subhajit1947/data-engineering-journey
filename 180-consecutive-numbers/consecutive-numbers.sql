# Write your MySQL query statement below
SELECT
 distinct num as ConsecutiveNums 
FROM
(
    SELECT
    *,
    LEAD(num) over(order by id) as frow,
    LEAD(num,2) over(order by id) as srow
    FROM Logs
) l
WHERE num=frow and frow=srow

