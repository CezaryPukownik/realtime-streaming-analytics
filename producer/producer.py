from confluent_kafka import Producer
import socket
import time

conf = {"bootstrap.servers": "kafka:9092", "client.id": socket.gethostname()}

producer = Producer(conf)

topic = "poc_topic"

try:
    while True:
        producer.produce(topic, "test message")
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    producer.flush()
