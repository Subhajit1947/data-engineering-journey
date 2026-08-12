-- Which city has the best customers? We would like to throw a promotional Music
-- Festival in the city we made the most money. Write a query that returns one city that
-- has the highest sum of invoice totals. Return both the city name & sum of all invoice
-- totals
SELECT 
billing_city,
ROUND(SUM(total)::numeric,2) as totals
FROM invoice
GROUP BY billing_city
ORDER BY totals DESC
LIMIT 1
