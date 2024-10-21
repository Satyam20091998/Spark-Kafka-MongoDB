# PySpark, Apache Kafka, and MongoDB Integration

## Project Overview

This project demonstrates the integration of **Apache Kafka**, **MongoDB**, and **Apache Spark** to process, store, and analyze data. The primary focus is on building a pipeline that ingests data from a Kafka producer, stores it in MongoDB, and uses Apache Spark for further processing.

## Objectives

- Set up a Kafka producer to stream data from local files.
- Store the produced data in MongoDB for persistence.
- Use Apache Spark to perform real-time data analysis on the ingested data.

## Key Components

1. **Kafka Producer and Consumer**:
   - Kafka is used as a message broker to handle the data streams.
   - Data is sent from a producer script, and a consumer reads it for further processing.
   
2. **MongoDB**:
   - MongoDB is used as a NoSQL database to store the streamed data for long-term persistence and retrieval.

3. **Apache Spark**:
   - Spark is used to perform operations and analytics on the data retrieved from Kafka and stored in MongoDB.

## Project Workflow

1. **Kafka Producer**: Reads data from local files and produces messages to Kafka topics.
2. **Kafka Consumer**: Consumes the messages from the Kafka topic and sends them to MongoDB.
3. **Spark Processing**: Spark retrieves the data from MongoDB for data processing and analytics.

## Architecture Diagram

![Architecture Diagram](https://github.com/Satyam20091998/Spark-Kafka-MongoDB/assets/92753984/8eb42cd8-ba27-4de8-87a1-7ca785e25ff3)

_Provide a detailed architecture diagram to showcase the components and data flow between Kafka, MongoDB, and Spark._

## File Structure

- `docker-compose.yml`: Defines the Docker setup for Kafka, Zookeeper, and MongoDB.
- `kafka_json_producer.py`: Kafka producer that reads local files and sends data to Kafka topics.
- `kafka_json_consumer.py`: Kafka consumer that reads the Kafka messages and inserts them into MongoDB.
- `spark.py`: Script that uses Apache Spark to perform operations on data stored in MongoDB.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/Satyam20091998/Spark-Kafka-MongoDB.git
    ```
2. Start Kafka, Zookeeper, and MongoDB using Docker:
    ```bash
    docker-compose up
    ```
3. Run the Kafka producer to stream data:
    ```bash
    python kafka_json_producer.py
    ```
4. Run the Kafka consumer to insert data into MongoDB:
    ```bash
    python kafka_json_consumer.py
    ```
5. Use Spark to process data:
    ```bash
    python spark.py
    ```

## Future Enhancements

- Implement more complex data transformations using Spark.
- Add real-time analytics and dashboards.
- Improve scalability by deploying on a distributed cluster.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Steps to setup projects

1.Using a local file will write a producer file for the kafka using kafka topic

2.then will load the produced data in mongo db

3. then  using spark will perform operations.

![Screenshot (7)](https://github.com/Satyam20091998/Spark-Kafka-MongoDB/assets/92753984/41ea8c46-3abe-4016-955e-10382e6e59ea)

![Screenshot (6)](https://github.com/Satyam20091998/Spark-Kafka-MongoDB/assets/92753984/4e2fa654-e3d8-4d50-aeba-a10fd03c5812)
