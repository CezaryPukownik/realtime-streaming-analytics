from confluent_kafka import Consumer
from clickhouse_driver import Client

kafka_conf = {
    "bootstrap.servers": "kafka:9092",
    "group.id": "poc-group",
    "default.topic.config": {"auto.offset.reset": "smallest"},
}

ch_client = Client(host="clickhouse")

consumer = Consumer(kafka_conf)
consumer.subscribe(["poc_topic"])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            break

        ch_client.execute(
            "INSERT INTO poc.events (id, timestamp, data) VALUES",
            [(str(msg.key()), msg.timestamp()[1], msg.value().decode("utf-8"))],
        )
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
