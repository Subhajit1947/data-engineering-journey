cs=["customer_id","product_key"]
cd=[
[1,5],   
[2,6],   
[3,5],   
[3,6],   
[1,6],   
]
c_df=spark.createDataFrame(cd,cs)
ps=["product_key"]
pd=[
[5],           
[6],          
]
p_df=spark.createDataFrame(pd,ps)

from pyspark.sql.functions import *
c_p=p_df.distinct().count()
c_df.groupBy(col("customer_id"))\
    .agg(countDistinct("*").alias("cpb"))\
    .filter(col("cpb")==c_p).select("customer_id").show()

