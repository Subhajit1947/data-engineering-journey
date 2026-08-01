s=["account_id","income"]
d=[
[3,108939],
[2,12747],
[8,87709],
[6,91796],
]
df=spark.createDataFrame(d,s)
c=[
["Low Salary"],
["Average Salary"],
["High Salary"]
]
c_df=spark.createDataFrame(c,["category"])

from pyspark.sql.functions import *
df=df.withColumn("category",
            when(col("income")<20000,"Low Salary")\
            .when((col("income")>=20000)&(col("income")<=50000),"Average Salary")\
            .otherwise("High Salary")
            )
c_df.join(df,"category","left")\
    .groupBy("category")\
    .agg(count("account_id").alias("accounts_count"))\
    .select(
        "category",
        "accounts_count"
    ).show()

