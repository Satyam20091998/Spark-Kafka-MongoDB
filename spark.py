from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("MongoDB to DataFrame") \
    .config("spark.mongodb.input.uri", "mongodb+srv://satyammarkam123:jacob@cluster0.fh8hexa.mongodb.net/?retryWrites=true&w=majority") \
    .getOrCreate()

# Read the MongoDB table into a DataFrame
df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()

# Perform operations on the DataFrame
# For example, display the first 10 rows
df.show(10)

# Close the SparkSession
spark.stop()
