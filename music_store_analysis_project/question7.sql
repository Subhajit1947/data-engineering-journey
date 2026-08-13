-- Return all the track names that have a song length longer than the average song length. 
-- Return the Name and Milliseconds for each track. Order by the song length with the 
-- longest songs listed first 

SELECT
name,milliseconds
FROM
(
    SELECT 
    *,AVG(milliseconds) over() as avg_time
    FROM track
)t
WHERE milliseconds>avg_time
ORDER BY milliseconds DESC