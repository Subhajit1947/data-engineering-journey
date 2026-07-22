#this is executed in databricks


from pyspark.sql.functions import *


s=["id","p_id"]
d=[
[1,None],
[2,1],
[3,1],
[4,2],
[5,2],
]

df=spark.createDataFrame(d,s)

p_df=df.filter(col("p_id").isNotNull()).select(col("p_id").alias("parent_id")).distinct()
df.join(p_df,df["id"]==p_df["parent_id"],"left")\
    .withColumn("type",
                when(col("p_id").isNull(),'Root')\
                .when(col("parent_id").isNotNull(),"Inner")\
                .otherwise("leaf")
    ).select("id","type").show()