
WITH tripcd as(
    SELECT
    t.id,t.client_id,t.driver_id,t.status,t.request_at 
    FROM Trips t
        join Users c
        on t.client_id=c.users_id
        join Users d
        on t.driver_id=d.users_id
    WHERE 
        c.banned='No' 
        and 
        d.banned='No'
        and request_at between "2013-10-01" and "2013-10-03"
)

SELECT
request_at as Day,
round(sum(CASE WHEN status='cancelled_by_driver' or status='cancelled_by_client' then 1 ELSE 0 END)/count(*),2) as 'Cancellation Rate'
FROM tripcd t
group by request_at


