import pyspark.sql.functions as F

(df.groupBy('Market Segment').agg(*[F.first(x,ignorenulls=True) for x in df.columns if x!='Market Segment'])
.show())