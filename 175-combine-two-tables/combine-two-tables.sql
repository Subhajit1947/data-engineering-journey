-- Write your PostgreSQL query statement below
SELECT 
    firstName,
    lastName,
    city,
    state    
FROM Person a
LEFT JOIN Address p
ON a.personId=p.personId