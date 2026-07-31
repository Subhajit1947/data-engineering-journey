# Write your MySQL query statement below
select
stock_name,sum(sellprice)-sum(buyprice) as capital_gain_loss 
from
(
SELECT
stock_name,case when operation='Sell' then sum(price) else 0 end as sellprice,
case when operation='Buy' then sum(price) else 0 end as buyprice
FROM Stocks 
GROUP BY stock_name,operation 
) s
group by stock_name



