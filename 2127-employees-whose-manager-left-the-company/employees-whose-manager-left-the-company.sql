-- Write your PostgreSQL query statement below
SELECT 
    employee_id 
FROM Employees
where salary<30000 and manager_id is not null and manager_id  not in (SELECT employee_id FROM Employees)
order By employee_id



