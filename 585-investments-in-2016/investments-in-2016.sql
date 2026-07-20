
SELECT 
round(sum(tiv_2016),2) as tiv_2016    
FROM Insurance
WHERE tiv_2015 IN (
    SELECT
    tiv_2015
    FROM Insurance
    group by tiv_2015    
    having count(*)>1
) AND (lat,lon) IN (
    SELECT 
    lat,lon
    FROM Insurance
    group by lat,lon
    having count(*)=1
)


