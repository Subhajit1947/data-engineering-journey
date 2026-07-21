# Write your MySQL query statement below
SELECT 
r_id as id,count("*") as num
FROM
((SELECT
    requester_id as r_id,accepter_id as a_id
FROM RequestAccepted)
UNION ALL
(SELECT
accepter_id as r_id,requester_id as a_id
FROM RequestAccepted)) a
GROUP BY r_id
order by num desc
limit 1
