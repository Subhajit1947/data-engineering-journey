#this is executed in databricks


from pyspark.sql.functions import *
s=["id","student"]
d=[
[1,"Abbot"],
[2,"Doris"],
[3,"Emerson"],
[4,"Green"],
[5,"Jeames"],
]
df=spark.createDataFrame(d,s)
a=df.agg(max("id").alias("max_id")).first()["max_id"]
df.withColumn("id",
        when(col("id")%2==0,col("id")-1)\
        .when((col("id")%2==1) & (col("id")<a),col("id")+1)\
        .otherwise(col("id")))\
        .orderBy(col("id"))\
        .show()