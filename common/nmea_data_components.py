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

    def to_signed_lat(self):
        value = self.degrees + self.minutes / 60
        return value if self.lat_dir == Hemisphere.NORTH else -value


@dataclass
class Longitude:
    degrees: int        = None
    minutes: float      = None
    lon_dir: Hemisphere = None

    def to_signed_lon(self):
        value = self.degrees + self.minutes / 60
        return value if self.lon_dir == Hemisphere.EAST else -value


@dataclass
class Coordinates:
    lat: Latitude   = None
    lon: Longitude  = None



@dataclass
class SatelliteInfo:
    satellite_id: int = None
    elevation: int = None
    azimuth: int = None
    snr: int = None