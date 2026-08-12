---What are top 3 values of total invoice?
SELECT
COUNT(*) AS invoices_count
FROM invoice
GROUP BY billing_country
ORDER BY invoices_count desc
LIMIT 3