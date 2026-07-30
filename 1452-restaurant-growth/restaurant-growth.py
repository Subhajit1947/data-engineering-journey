s=["customer_id","name","visited_on","amount"]
d=[
    [1,"Jhon","2019-01-01",100],
    [2,"Daniel","2019-01-02",110],
    [3,"Jade","2019-01-03",120],
    [4,"Khaled","2019-01-04",130],
    [5,"Winston","2019-01-05",110], 
    [6,"Elvis","2019-01-06",140], 
    [7,"Anna","2019-01-07",150],
    [8,"Maria","2019-01-08",80 ],
    [9,"Jaze","2019-01-09",110], 
    [1,"Jhon","2019-01-10",130], 
    [3,"Jade","2019-01-10",150] 
]
df=spark.createDataFrame(d,s)

from pyspark.sql.functions import *
from pyspark.sql.window import Window
window=Window.orderBy("day_key").rangeBetween(-6,0)
df.groupBy("visited_on").agg(sum("amount").alias("daily_amount"))\
    .withColumn("day_key",datediff("visited_on",lit("1970-01-01")))\
    .withColumn("amount",sum("daily_amount").over(window))\
    .withColumn("windowcount",count("daily_amount").over(window))\
    .filter(col("windowcount")==7)\
    .select(
        "visited_on",
        "amount",
        round(col("amount")/7,2).alias("average_amount")
    ).show()


