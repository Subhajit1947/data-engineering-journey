s=["stock_name","operation","operation_day","price"]
d=[
["Leetcode","Buy",1 ,1000 ],
["Corona Masks","Buy",2 ,10   ],
["Leetcode","Sell",5 ,9000 ],
["Handbags","Buy",17,30000],
["Corona Masks","Sell",3 ,1010 ],
["Corona Masks","Buy",4 ,1000 ],
["Corona Masks","Sell",5 ,500  ],
["Corona Masks","Buy",6 ,1000 ],
["Handbags","Sell",29,7000 ],
["Corona Masks","Sell",10,10000],
]
df=spark.createDataFrame(d,s)


from pyspark.sql.functions import *
df.groupBy("stock_name")\
    .agg(sum(when(col("operation")=="Sell",col("price")).otherwise(-col("price"))).alias("capital_gain_loss"))\
    .show()
