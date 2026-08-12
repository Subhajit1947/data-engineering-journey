----Who is the senior most employee based on job title?

SELECT 
first_name||' '||last_name AS name
FROM employee
ORDER BY levels desc
LIMIT 1