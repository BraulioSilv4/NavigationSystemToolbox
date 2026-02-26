from common.nmea_types import GGA, NMEAInstance, Coordinates, FixQuality, Altitude, DistanceMeasureUnit, Checksum

def GGA_parser(instance: NMEAInstance):
    data, checksum = instance.nmea_str.split('*')
    data = data.split(',')
    gga_data: GGA = GGA()

    gga_data.checksum = Checksum(checksum)
    if not gga_data.checksum.validate_checksum(instance.nmea_str):
        print("Invalid checksum for GGA sentence!")
        return

    gga_data.utc = data[1]
    gga_data.coordinates = Coordinates(data[2], data[3], data[4], data[5])
    gga_data.fix_quality = FixQuality(int(data[6]))
    gga_data.num_satellites = int(data[7])
    gga_data.hdop = float(data[8])
    gga_data.altitude = Altitude(float(data[9]), DistanceMeasureUnit(data[10]))
    gga_data.geoid_height = Altitude(float(data[11]), DistanceMeasureUnit(data[12]))
    gga_data.time_since_last_dgps = float(data[13]) if data[13] else None
    gga_data.dgps_reference_station_id = data[14] if data[14] else None
