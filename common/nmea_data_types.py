from dataclasses import dataclass
from datetime import time
from common.nmea_data_components import Coordinates, Altitude, Checksum
from common.nmea_enum import FixQuality


@dataclass
class GGA:
    utc: time = None
    coordinates: Coordinates = None
    fix_quality: FixQuality = None
    num_satellites: int = None
    hdop: float = None
    altitude: Altitude = None
    geoid_height: Altitude = None
    time_since_last_dgps: float = None
    dgps_reference_station_id: str = None
    checksum: Checksum = None



@dataclass
class RMC:
    lat: float = None
    lat_dir: str = None
    lon: float = None
    lon_dir: str = None
    speed: float = None
    course: float = None
