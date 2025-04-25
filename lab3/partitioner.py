# partitioner.py
def station_partitioner(key, all_partitions, available_partitions):
    """Partition based on station name."""
    station = key.decode("utf-8")
    if station == "SVDT1":
        return 0
    elif station in ["SVDT2", "SVDT3"]:  # Add more stations as needed
        return 1
    return 0  # Default fallback