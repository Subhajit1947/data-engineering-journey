s=["person_id","person_name","weight","turn"]
d=[
[5,"Alice",250,1],
[4,"Bob",175,5],
[3,"Alex",350,2],
[6,"John Cena",400,3],
[1,"Winston",500,6],
[2,"Marie",200,4],
]
df=spark.createDataFrame(d,s)


from pyspark.sql.functions import *
from pyspark.sql.window import Window
window=Window.orderBy("turn")
df.withColumn("cumulativesum",sum("weight").over(window))\
    .filter(col("cumulativesum")<=1000)\
    .orderBy(col("cumulativesum").desc()).limit(1).select("person_name").show()