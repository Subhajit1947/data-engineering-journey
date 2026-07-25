# Write your MySQL query statement below

SELECT 
customer_id 
FROM Customer
group by customer_id 
having count(distinct(product_key))=(select count(distinct product_key) from product)


