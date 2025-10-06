# Stock Streaming and Visualization Project

## **Description**
This project streams stock data, processes micro-batches using Apache Spark, and visualizes the average stock prices using **Matplotlib** in Python.  
It enables real-time visualization of stock trends from the last 5 micro-batches. The project uses **Kafka** for streaming, **Spark** for processing, and **Matplotlib** for interactive visualization.

---

## **Table of Contents**
1. [Project Structure](#project-structure)  
2. [Requirements](#requirements)  
3. [Setup](#setup)  
4. [Running the Kafka Producer](#running-the-kafka-producer)  
5. [Processing Micro-Batches](#processing-micro-batches)  
6. [Visualizing Data](#visualizing-data)  
7. [Notes / Tips](#notes--tips)  

---


stock_streaming_project/
│
├── data/
│ └── stocks.csv # Static CSV for simulation / raw stock data
│
├── kafka_producer/
│ └── stock_producer.py # Sends data to Kafka topic
│
├── spark_consumer/
│ └── spark_stream_processor.py # PySpark reads from Kafka and processes micro-batches
│
├── output/ # Spark stores processed micro-batch CSVs here
│
├── visualize_stock.py # Python script for plotting data
├── README.md # Project documentation
└── venv/ # Python virtual environment

-----

**Kafka and Zookeeper**

Install kafka first

**Change directory to the Kafka**

cd ~/kafka_2.13-3.9.0

**Start Zookeeper**

bin/zookeeper-server-start.sh config/zookeeper.properties

**Start Kafka broker**

kafka-server-start.sh config/server.properties

**Create a Kafka topic**

kafka-topics.sh --create --topic stockTopic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1


**Console input**

bin/kafka-console-producer.sh --topic tweets --bootstrap-server localhost:9092

**Start Hadoop HDFS**

start-dfs.sh


***HDF**

source ~/.bashrc


**Create a directory in HDFS for Spark output**

hdfs dfs -mkdir -p /user/yukesh/stock_streaming_project/output

**List the main project directory:**

hdfs dfs -ls /user/yukesh/stock_streaming_project/


**List the Spark output directory:**
hdfs dfs -ls /user/yukesh/stock_streaming_project/output


**Upload the stock CSV data to HDFS:**

hdfs dfs -put ./data/stocks.csv /user/yukesh/stock_streaming_project/data/

**4. View Files in HDFS**
hdfs dfs -cat /user/yukesh/stock_streaming_project/output/part-00000-*.csv


## Spark Commands for Stock Streaming Project

This project uses **PySpark Structured Streaming** to read from Kafka, process stock data, and write micro-batch outputs to HDFS.

---


### Home setup JAVA 17

export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin


***Envirment Setup***
python3 -m venv spark-venv

### 1. Start Spark Submit for Streaming
Run your Spark consumer/processor script:
```bash
spark-submit \
  --master local[*] \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2 \
  spark_consumer/spark_stream_processor.py

or

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 spark_stream_processor.py


### Visualisation 

python3 -m venv venv

python3 visualize_stock.py


## 📊 Data Visualization Results

After running the Spark Streaming process, the results are visualized using **Matplotlib**.

### 1️⃣ Average Stock Price (Last Batch)
This bar chart shows the average price of each stock in the latest micro-batch.

![Average Price Last Batch](images/avg_price_last_batch.png)

---

### 2️⃣ Average Stock Price Trend (Last 5 Micro-Batches)
This line graph shows the price trend of each stock over the last 5 micro-batches, helping visualize fluctuations over time.

![Average Price Trend](images/avg_price_trend.png)

---

### 3️⃣ HDFS Node Overview
This image shows the HDFS node where Spark stores micro-batch outputs.

![HDFS Node](images/HDFS%20node.png)

---

### 4️⃣ Kafka Streaming Setup
This screenshot represents the Kafka streaming process that continuously produces stock data.

![Kafka Streaming](images/kafka%20streaming.png)





