-- Who is the best customer? The customer who has spent the most money will be
-- declared the best customer. Write a query that returns the person who has spent the
-- most money


SELECT
c.customer_id,c.first_name,c.last_name,
ROUND(sum(i.total)::numeric,2) as totals
FROM customer c
    join invoice i
    ON c.customer_id=i.customer_id
GROUP BY c.customer_id
ORDER BY totals DESC
LIMIT 1




