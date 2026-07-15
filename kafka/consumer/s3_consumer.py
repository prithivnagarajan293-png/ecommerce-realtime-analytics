import json
from datetime import datetime

import boto3
from confluent_kafka import Consumer

from config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    S3_BUCKET,
    AWS_REGION,
)

consumer = Consumer({
    "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
    "group.id": "s3-consumer",
    "auto.offset.reset": "latest"
})

consumer.subscribe([KAFKA_TOPIC])

s3 = boto3.client("s3", region_name=AWS_REGION)

batch = []

print("S3 Consumer Started...")

while True:

    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    order = json.loads(msg.value().decode("utf-8"))

    batch.append(order)

    print(f"Collected {len(batch)}/10")

    if len(batch) == 10:

        file_name = (
            f"raw/orders_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        s3.put_object(
            Bucket=S3_BUCKET,
            Key=file_name,
            Body=json.dumps(batch, indent=2)
        )

        print(f"Uploaded {file_name}")

        batch = []