-- Write your PostgreSQL query statement below
WITH ctg as(
    SELECT
        *
    FROM (
        VALUES
        ('Low Salary'),
        ('Average Salary'),
        ('High Salary')
    ) as c(category)
),
ctg2 AS(
SELECT 
*,
CASE 
    WHEN income<20000 THEN 'Low Salary' 
    WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
    ELSE 'High Salary'
END AS category
FROM Accounts 
) 

SELECT 
c1.category,count(c2.category) as accounts_count 
FROM ctg c1 left join ctg2 c2
ON c1.category=c2.category
GROUP BY c1.category

