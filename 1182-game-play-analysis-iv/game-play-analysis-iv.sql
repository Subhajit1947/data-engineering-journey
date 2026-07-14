

SELECT
round(count(distinct case when b.event_date=date_add(a.first_login,INTERVAL 1 day) then a.player_id end)/count(distinct a.player_id),2) as fraction
FROM Activity b join
(
SELECT
player_id,MIN(event_date) as first_login
FROM Activity
GROUP BY player_id 
)a
on b.player_id=a.player_id

