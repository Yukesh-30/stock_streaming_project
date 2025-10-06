from kafka import KafkaProducer
import time
import csv
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open('../data/stocks.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        producer.send('stockTopic', value=row)
        print(f"Sent: {row}")
        time.sleep(1)

producer.flush()
