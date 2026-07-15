# Write your MySQL query statement below

SELECT
e1.name
FROM Employee e1 
join
(SELECT
    managerId as id
FROM Employee 
    WHERE managerId IS NOT NULL
    GROUP BY managerId   
    HAVING COUNT(*)>4
)e2
ON e1.id=e2.id
