from enum import Enum
from typing import Union

class Checksum:
    def __init__(self, value: str):
        if value is not None:
            self.value = hex(int(value, 16))

    value = None

    def validate_checksum(self, sentence: str) -> bool:
        if self.value is None:
            print("No checksum value provided for validation!")
            return False

        checksum = 0
        for c in range(len(sentence)):
            if sentence[c] == '*':
                break

            if sentence[c] == '$':
                continue

            checksum ^= ord(sentence[c])

        return hex(checksum) == self.value


class DistanceMeasureUnit(Enum):
    METERS = 'M'
    FEET = 'F'


class Altitude:
    def __init__(self, value: float, unit: DistanceMeasureUnit):
        self.unit = unit
        self.value = value

    unit: DistanceMeasureUnit = None
    value: float = None


class FixQuality(Enum):
    INVALID = 0
    GPS_FIX = 1
    DGPS_FIX = 2


class Coordinates:
    def __init__(self, lat: str, lat_dir: str, lon: str, lon_dir: str):
        self.lat = float(lat)
        self.lat_dir = lat_dir
        self.lon = float(lon)
        self.lon_dir = lon_dir

    lat: float = None
    lat_dir: str = None
    lon: float = None
    lon_dir: str = None


class GGA:
    utc: str = None
    coordinates: Coordinates = None
    fix_quality: FixQuality = None
    num_satellites: int = None
    hdop: float = None
    altitude: Altitude = None
    geoid_height: Altitude = None
    time_since_last_dgps: float = None
    dgps_reference_station_id: str = None
    checksum: Checksum = None


class RMC:
    lat: float = None
    lat_dir: str = None
    lon: float = None
    lon_dir: str = None
    speed: float = None
    course: float = None


class NMEAInstance:
    def __init__(self, data):
        self.nmea_str = data
        self.constellation = data[1:3]
        self.type = data[3:6]


    constellation: str = None
    type: str = None
    nmea_str: str = None
    data: Union[GGA, RMC] = None

    def parse(self):
        if self.nmea_str is None:
            print("No valid data to construct instance!")
            return

        if self.type == "GGA":
            from .nmea_parsers import GGA_parser
            GGA_parser(self)

        return