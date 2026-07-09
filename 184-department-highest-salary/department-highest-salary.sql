# Write your MySQL query statement below
SELECT
dept_name as Department,
name as Employee,
salary as Salary 
FROM
(SELECT
    e.id,e.name,e.salary,e.departmentId,d.name as dept_name,
    dense_rank() over(partition by d.name order by e.salary desc) as rnk
FROM Employee e join Department d
    on e.departmentId=d.id
) em
WHERE 
rnk=1


