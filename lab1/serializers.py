# serializers.py
import json

from models import Air, Earth, Water

def serializer(obj):
    """Serialize object to JSON byte string."""
    serialized = json.dumps({
        "type": obj.__class__.__name__,
        "data": obj.__dict__
    }).encode("utf-8")
    print(f"Serialized {obj.__class__.__name__}: {serialized.decode('utf-8')}")  # Debug
    return serialized

def deserializer(data):
    decoded = json.loads(data.decode("utf-8"))
    data_dict = decoded["data"]
    normalized = {}
    for k, v in data_dict.items():
        if k.lower() == "ph":
            normalized["pH"] = v
        elif k.lower() == "pm2_5" or k == "PM2_5":
            normalized["PM2_5"] = v
        elif k.lower() == "do":
            normalized["DO"] = v
        else:
            # Preserve original key if it matches models.py, otherwise normalize
            if k in ["Time", "Station", "Moisture", "Temperature", "Salinity", "pH", 
                     "Water_Root", "Water_Leaf", "Water_Level", "Voltage", 
                     "Light", "Total_Rainfall", "Rainfall", "Wind_Direction", 
                     "PM2_5", "PM10", "CO", "NOx", "SO2", "DO"]:
                normalized[k] = v
            else:
                normalized[k.capitalize()] = v
    if decoded["type"] == "Air":
        return Air(**normalized)
    elif decoded["type"] == "Earth":
        return Earth(**normalized)
    elif decoded["type"] == "Water":
        return Water(**normalized)
    return None