from typing import Union
from common.nmea_data_components import Constellation
from common.nmea_data_types import GGA, RMC


class NMEAInstance:
    def __init__(self, data):
        self.nmea_str = data
        self.constellation = data[1:3]
        self.type = data[3:6]


    constellation: Constellation = None
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