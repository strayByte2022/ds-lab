from kafka import KafkaConsumer, KafkaProducer
from serializers import deserializer, serializer
import numpy as np
import threading
from kafka.errors import NoBrokersAvailable
import os
def impute_missing_values(obj):
    if obj is None:
        return None
    numeric_fields = [field for field in dir(obj) if isinstance(getattr(obj, field), (int, float)) or getattr(obj, field) is None]
    # Filter out non-writable attributes
    numeric_fields = [field for field in numeric_fields if isinstance(getattr(obj, field, None), (int, float, type(None))) and not field.startswith('__')]
    values = [getattr(obj, field) for field in numeric_fields if getattr(obj, field) is not None]
    mean = np.nanmean(values) if values else 0

    for field in numeric_fields:
        if getattr(obj, field) is None:
            setattr(obj, field, mean)
    return obj


def consume(topic):
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers="localhost:9092",
            group_id="env_group",
            value_deserializer=deserializer,
        )
    except NoBrokersAvailable:
        print("Kafka broker not available")
        return

    producer = KafkaProducer(
        bootstrap_servers="localhost:19092",
        value_serializer=serializer
    )


    for msg in consumer:

        obj = msg.value
        print(f"Received {topic} message: {obj.__dict__}")
        processed = impute_missing_values(obj)
        print(f"Processed {topic} message: {processed.__dict__}")
        producer.send(f"processed_{topic}", value=processed)
        print(f"Sent processed {topic} message to Kafka")

        os.makedirs("result/file", exist_ok=True)
        with open(f"result/file/{topic}_imputed.txt", "a") as f:
            f.write(processed.__dict__.__str__() + "\n")
        print(f"Saved processed {topic} message to file")

topics = ["Air", "Earth", "Water"]
threads = []

for topic in topics:
    t = threading.Thread(target=consume, args=(topic,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
