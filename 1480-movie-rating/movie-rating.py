ms=["movie_id","title"]       
md=[
[1,"Avengers"],
[2,"Frozen 2"],
[3,"Joker"],
]
m_df=spark.createDataFrame(md,ms)
us=["user_id","name"]
ud=[
[1,"Daniel"],
[2,"Monica"],
[3,"Maria"],
[4,"James"],
]
u_df=spark.createDataFrame(ud,us)

mrs=["movie_id","user_id","rating","created_at"]
mrd=[
[1,1,3,"2020-01-12"],
[1,2,4,"2020-02-11"],
[1,3,2,"2020-02-12"],
[1,4,1,"2020-01-01"],
[2,1,5,"2020-02-17"], 
[2,2,2,"2020-02-01"], 
[2,3,2,"2020-03-01"],
[3,1,3,"2020-02-22"], 
[3,2,4,"2020-02-25"], 
]
mr_df=spark.createDataFrame(mrd,mrs)

from pyspark.sql.functions import *
muc=mr_df.groupBy("user_id")\
    .agg(count("movie_id").alias("mrcount"))\
    .select("user_id","mrcount")
name=muc.join(u_df,"user_id","inner")\
    .orderBy(col("mrcount").desc(),"name")\
    .select("name")\
    .limit(1)\
    .collect()[0][0]
amr=mr_df.filter((month("created_at")==2) & (year("created_at")==2020)).groupBy("movie_id")\
    .agg(avg("rating").alias("avg_rating"))\
    .select("movie_id","avg_rating")
title=amr.join(m_df,"movie_id","inner")\
    .orderBy(col("avg_rating").desc(),"title")\
    .select("title")\
    .limit(1)\
    .collect()[0][0]
result=spark.createDataFrame([[name],[title]],["results"])
result.show()


