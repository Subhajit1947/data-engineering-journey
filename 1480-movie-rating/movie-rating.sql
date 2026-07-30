# Write your MySQL query statement below
(select 
name as results
from
(
select 
user_id,count("*") as ratecount
from
    MovieRating
    group by user_id       
) mr join Users u
on mr.user_id=u.user_id
order by mr.ratecount desc,name limit 1)
union all
(select
title
from
(
select
movie_id,avg(rating) as avg_rating
from MovieRating 
where month(created_at)=2 and year(created_at)=2020
group by movie_id 
)mrr join Movies m
on mrr.movie_id=m.movie_id
order by avg_rating desc,title limit 1
)