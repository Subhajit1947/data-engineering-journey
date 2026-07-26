url="/Volumes/workspace/default/de-project-volume/sales_data.csv"
s_df=spark.read.format("csv")\
                .option("inferSchema","true")\
                .option("header","true")\
                .load(url)
s_df.show(5)

from pyspark.sql.functions import *
from pyspark.sql.window import Window
window=Window.partitionBy(col("product_id")).orderBy("year")
s_df.withColumn("rnk",rank().over(window))\
    .filter(col("rnk")==1)\
    .select(
        "product_id",
        col("year").alias("first_year"),
        "quantity",
        "price"
    ).show()

