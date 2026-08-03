ss=['user_id','time_stamp']
sd=[
[3,"2020-03-21", "10:16:13"],
[7,"2020-01-04", "13:57:59"],
[2,"2020-07-29", "23:09:44"],
[6,"2020-12-09", "10:39:37"],
]
s_df=spark.createDataFrame(sd,ss)
c_s=['user_id','time_stamp','action']
c_d=[
[3,"2021-01-06 03:30:46","timeout"],
[3,"2021-07-14 14:00:00","timeout"],
[7,"2021-06-12 11:57:29","confirmed"],
[7,"2021-06-13 12:58:28","confirmed"],
[7,"2021-06-14 13:59:27","confirmed"],
[2,"2021-01-22 00:00:00","confirmed"],
[2,"2021-02-28 23:59:59","timeout"],
]
c_df=spark.createDataFrame(c_d,c_s)
from pyspark.sql.functions import *

result_df = s_df.join(c_df, "user_id", "left")\
    .groupBy("user_id") \
    .agg(round(avg(when(col("action") == "confirmed", 1.0).otherwise(0)), 2).alias("confirmation_rate"))

result_df.show()

