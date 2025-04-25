import json
from confluent_kafka import SerializingProducer, DeserializingConsumer
from confluent_kafka.serialization import StringSerializer, StringDeserializer

# Data classes
class AirData:
    def __init__(self, time, station, temperature, moisture, light, total_rainfall, rainfall, wind_direction, pm25, pm10, co, nox, so2):
        self.timestamp = time
        self.station = station
        self.type = "air"
        self.value = {
            "temperature": float(temperature),
            "moisture": float(moisture),
            "light": float(light),
            "total_rainfall": float(total_rainfall),
            "rainfall": float(rainfall),
            "wind_direction": float(wind_direction),
            "pm25": float(pm25),
            "pm10": float(pm10),
            "co": float(co),
            "nox": float(nox),
            "so2": float(so2)
        }

class EarthData:
    def __init__(self, time, station, moisture, temperature, salinity, ph, water_root, water_leaf, water_level, voltage):
        self.timestamp = time
        self.station = station
        self.type = "earth"
        self.value = {
            "moisture": float(moisture),
            "temperature": float(temperature),
            "salinity": float(salinity),
            "ph": float(ph),
            "water_root": float(water_root),
            "water_leaf": float(water_leaf),
            "water_level": float(water_level),
            "voltage": float(voltage)
        }

class WaterData:
    def __init__(self, time, station, ph, do, temperature, salinity):
        self.timestamp = time
        self.station = station
        self.type = "water"
        self.value = {
            "ph": float(ph),
            "do": float(do),
            "temperature": float(temperature),
            "salinity": float(salinity)
        }

# Custom Serializer
def object_to_json(obj, ctx):
    if obj is None:
        return None
    return json.dumps({
        "timestamp": obj.timestamp,
        "station": obj.station,
        "type": obj.type,
        "value": obj.value
    }).encode('utf-8')

# Custom Deserializer
def json_to_object(msg_value, ctx):
    if msg_value is None:
        return None
    data = json.loads(msg_value.decode('utf-8'))
    if data["type"] == "air":
        v = data["value"]
        return AirData(
            data["timestamp"], 
            data["station"],
            v["temperature"],
            v["moisture"],
            v["light"],
            v["total_rainfall"],
            v["rainfall"],
            v["wind_direction"],
            v["pm25"],
            v["pm10"],
            v["co"],
            v["nox"],
            v["so2"]
        )
    elif data["type"] == "earth":
        v = data["value"]
        return EarthData(
            data["timestamp"],
            data["station"],
            v["moisture"],
            v["temperature"],
            v["salinity"],
            v["ph"],
            v["water_root"],
            v["water_leaf"],
            v["water_level"],
            v["voltage"]
        )
    elif data["type"] == "water":
        v = data["value"]
        return WaterData(
            data["timestamp"],
            data["station"],
            v["ph"],
            v["do"],
            v["temperature"],
            v["salinity"]
        )
    return None

# Custom Partitioner
def custom_partitioner(key, all_partitions, available_partitions):
    station = key.decode('utf-8')  # Key is the station ID
    return all_partitions[hash(station) % len(all_partitions)]