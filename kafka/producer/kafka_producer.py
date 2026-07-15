import json
import time
import sys
import os

from confluent_kafka import Producer

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
from producer.order_generator import generate_order


def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Sent Order {msg.key()} to {msg.topic()} [{msg.partition()}]")


producer = Producer({
    "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS
})

print("Producer Started...\n")

while True:

    order = generate_order()

    producer.produce(
        topic=KAFKA_TOPIC,
        value=json.dumps(order),
        callback=delivery_report
    )

    producer.poll(0)

    print(order)

    time.sleep(1)