from dataclasses import dataclass
from common.nmea_enum import DistanceMeasureUnit, Hemisphere


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

