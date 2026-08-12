----Which countries have the most Invoices?
SELECT
billing_country
FROM invoice
GROUP BY billing_country
ORDER BY COUNT(*) desc
LIMIT 1