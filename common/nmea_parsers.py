from datetime import time

from common.nmea_data_components import Coordinates, Altitude, FixQuality, DistanceMeasureUnit, Checksum, Latitude, \
    Longitude, Hemisphere
from common.nmea_data_types import GGA
from common.nmea_instance import NMEAInstance

def GGA_parser(instance: NMEAInstance):
    data, checksum = instance.nmea_str.split('*')
    data = data.split(',')
    gga_data: GGA = GGA()

    gga_data.checksum = Checksum(int(checksum, 16))
    if not gga_data.checksum.validate_checksum(instance.nmea_str):
        print("Invalid checksum for GGA sentence!")
        return

    gga_data.utc = time(
        hour=int(data[1][0:2]),
        minute=int(data[1][2:4]),
        second=int(data[1][4:6]),
        microsecond=int(data[1].split('.')[1])
    )

    gga_data.coordinates = Coordinates(
        Latitude(int(data[2][0:2]), float(data[2][2:]) , Hemisphere(data[3])),
        Longitude(int(data[4][0:3]), float(data[4][3:]), Hemisphere(data[5]))
    )

    gga_data.fix_quality = FixQuality(int(data[6]))
    gga_data.num_satellites = int(data[7])
    gga_data.hdop = float(data[8]) if data[8] else None
    gga_data.altitude = Altitude(float(data[9]), DistanceMeasureUnit(data[10]))
    gga_data.geoid_height = Altitude(float(data[11]), DistanceMeasureUnit(data[12]))
    gga_data.time_since_last_dgps = float(data[13]) if data[13] else None
    gga_data.dgps_reference_station_id = data[14] if data[14] else None
    NMEAInstance.data = gga_data
