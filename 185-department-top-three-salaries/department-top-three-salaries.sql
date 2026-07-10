# Write your MySQL query statement below

SELECT
dept as Department,
name as Employee,
salary as Salary
FROM
(
SELECT 
e.id,e.name,e.salary,d.name as dept,dense_rank() over(partition by d.name order by e.salary desc) as rnk
FROM
    Employee e join Department d
    on e.departmentId=d.id
)ed
WHERE rnk<4


