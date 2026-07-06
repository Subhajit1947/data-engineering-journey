
SELECT
    IFNULL(
(
    SELECT
        salary 
    FROM
        (
        SELECT 
        *,dense_rank() over(order by salary desc) as rnk
        FROM Employee E
        )e
    where rnk=2
    limit 1
),null) as SecondHighestSalary