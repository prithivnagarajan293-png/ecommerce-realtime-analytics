import json

from confluent_kafka import Consumer

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "bronze-consumer",
    "auto.offset.reset": "earliest"
})

consumer.subscribe(["orders"])

print("Consumer Started...")

while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    print(json.loads(msg.value().decode("utf-8")))