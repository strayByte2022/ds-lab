# consumer.py
from kafka import KafkaConsumer
from serializers import deserializer
import threading

def consume(topic, group_id="env_group"):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers="localhost:9092",
        group_id=group_id,
        value_deserializer=deserializer,
        auto_offset_reset="earliest"
    )
    print(f"Starting consumer for {topic}")
    for message in consumer:
        obj = message.value
        if obj is None:
            print(f"Error: Deserialized {topic} message is None - Raw: {message.value}")
        else:
            print(f"{topic} - Partition {message.partition}: {obj.__dict__}")

topics = ["Air", "Earth", "Water"]
threads = []

for topic in topics:
    t = threading.Thread(target=consume, args=(topic,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()