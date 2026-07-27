u_s=["user_id","join_date","favorite_brand"]
u=[
[1,"2018-01-01","Lenovo"],
[2,"2018-02-09","Samsung"],
[3,"2018-01-19","LG"],
[4,"2018-05-21","HP"],
]
u_df=spark.createDataFrame(u,u_s)
o_s=["order_id","order_date","item_id","buyer_id","seller_id"]
o=[
[1,"2019-08-01",4,1,2],
[2,"2018-08-02",2,1,3],
[3,"2019-08-03",3,2,3],
[4,"2018-08-04",1,4,2],
[5,"2018-08-04",1,3,4],
[6,"2019-08-05",2,2,4],
]
o_df=spark.createDataFrame(o,o_s)

from pyspark.sql.functions import *
u_df.join(o_df,[u_df["user_id"]==o_df["buyer_id"],year(o_df["order_date"])=='2019'],"left")\
    .groupBy("user_id","join_date")\
        .agg(count("order_date").alias("orders_in_2019"))\
        .select(
            col("user_id").alias("buyer_id"),
            "join_date",
            "orders_in_2019"
        ).show()


