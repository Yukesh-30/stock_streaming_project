from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg
from pyspark.sql.types import StructType, StringType, DoubleType, IntegerType

# Paths
OUTPUT_PATH = "/home/yukesh3012/stock_streaming_project/output"
CHECKPOINT_PATH = "/home/yukesh3012/stock_streaming_project/output/checkpoint"

# Create Spark session
spark = SparkSession.builder \
    .appName("StockStreamProcessor") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Define schema for stock data
schema = StructType() \
    .add("symbol", StringType()) \
    .add("price", StringType()) \
    .add("volume", StringType())

# Read data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "stockTopic") \
    .load()

# Parse Kafka value as JSON
json_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Convert columns to proper types
typed_df = json_df.withColumn("price", col("price").cast(DoubleType())) \
                  .withColumn("volume", col("volume").cast(IntegerType()))

# Compute running average price per symbol
agg_df = typed_df.groupBy("symbol").agg(avg("price").alias("avg_price"))

# Function to write each micro-batch to CSV
def write_to_csv(batch_df, batch_id):
    batch_df.coalesce(1).write.mode("append").option("header", True).csv(OUTPUT_PATH)

# Start streaming query
query = agg_df.writeStream \
    .outputMode("update") \
    .foreachBatch(write_to_csv) \
    .option("checkpointLocation", CHECKPOINT_PATH) \
    .start()

query.awaitTermination()

