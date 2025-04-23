# producer.py
import csv
from kafka import KafkaProducer
from models import Air, Earth, Water
from serializers import serializer
from partitioner import station_partitioner
from concurrent.futures import ThreadPoolExecutor

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=serializer,
    partitioner=station_partitioner
)

def send_data(file_path, topic, cls):
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"Raw CSV row for {topic}: {row}")  # Debug CSV input
            obj = cls(**row)
            print(f"Object dict for {topic}: {obj.__dict__}")  # Debug object attributes
            producer.send(topic, value=obj, key=obj.Station.encode("utf-8"))
    print(f"Finished sending {topic} data")

files = [
    ("AIR2308.csv", "Air", Air),
    ("EARTH2308.csv", "Earth", Earth),
    ("WATER2308.csv", "Water", Water),
]

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(lambda x: send_data(*x), files)

producer.flush()
print("All data sent!")