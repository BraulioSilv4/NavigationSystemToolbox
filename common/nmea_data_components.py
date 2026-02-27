from dataclasses import dataclass
from enum import Enum

@dataclass
class Checksum:
    value: int | None = None

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

        return checksum == self.value



class DistanceMeasureUnit(Enum):
    METERS  = 'M'
    FEET    = 'F'



class Constellation(Enum):
    GPS         = "GP"
    GLONASS     = "GL"
    GALILEO     = "GA"
    GNSS        = "GN"
    BEIDOU_GB   = "GB"
    BEIDOU_BD   = "BD"
    Loran_C     = "Loran C"
    EPIRB       = "EP"



class FixQuality(Enum):
    INVALID         = 0
    GPS_FIX         = 1
    DGPS_SPS        = 2
    PPS             = 3
    RTK_INT         = 4
    RTK_FLOAT       = 5
    DEAD_RECKONING  = 6
    MANUAL_INPUT    = 7
    SIM_MODE        = 8



class Hemisphere(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST  = 'E'
    WEST  = 'W'



@dataclass
class Altitude:
    value: float = None
    unit: DistanceMeasureUnit = None



@dataclass
class Latitude:
    degrees: int        = None
    minutes: float      = None
    lat_dir: Hemisphere = None



@dataclass
class Longitude:
    degrees: int        = None
    minutes: float      = None
    lon_dir: Hemisphere = None



@dataclass
class Coordinates:
    lat: Latitude   = None
    lon: Longitude  = None

