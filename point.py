class Point:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon
