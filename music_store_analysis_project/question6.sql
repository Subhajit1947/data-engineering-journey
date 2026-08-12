-- Write query to return the email, first name, last name, & Genre of all Rock Music
-- listeners. Return your list ordered alphabetically by email starting with A

SELECT
distinct c.email, c.first_name, c.last_name
FROM invoice i
    join invoice_line l
    on i.invoice_id=l.invoice_id
    join customer c
    on i.customer_id=c.customer_id
    join track t
    on l.track_id=t.track_id
    join genre g
    on t.genre_id=g.genre_id
WHERE g.name='Rock'
ORDER BY c.email
    



