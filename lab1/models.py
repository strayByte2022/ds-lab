# models.py
class Air:
    def __init__(self, Time, Station, Temperature, Moisture, Light, Total_Rainfall, Rainfall, Wind_Direction, PM2_5, PM10, CO, NOx, SO2):
        self.Time = Time
        self.Station = Station
        self.Temperature = Temperature
        self.Moisture = Moisture
        self.Light = Light
        self.Total_Rainfall = Total_Rainfall
        self.Rainfall = Rainfall
        self.Wind_Direction = Wind_Direction
        self.PM2_5 = PM2_5
        self.PM10 = PM10
        self.CO = CO
        self.NOx = NOx
        self.SO2 = SO2

class Earth:
    def __init__(self, Time, Station, Moisture, Temperature, Salinity, pH, Water_Root, Water_Leaf, Water_Level, Voltage):
        self.Time = Time
        self.Station = Station
        self.Moisture = Moisture
        self.Temperature = Temperature
        self.Salinity = Salinity
        self.pH = pH
        self.Water_Root = Water_Root
        self.Water_Leaf = Water_Leaf
        self.Water_Level = Water_Level
        self.Voltage = Voltage

class Water:
    def __init__(self, Time, Station, pH, DO, Temperature, Salinity):
        self.Time = Time
        self.Station = Station
        self.pH = pH
        self.DO = DO
        self.Temperature = Temperature
        self.Salinity = Salinity