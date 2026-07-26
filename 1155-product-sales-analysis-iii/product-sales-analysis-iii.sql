# Write your MySQL query statement below

SELECT 
product_id,
year as first_year,
quantity,
price 
FROM
(
    SELECT 
    *,RANK() OVER(PARTITION BY product_id ORDER BY year) as rnk
    FROM sales
) s WHERE rnk=1



