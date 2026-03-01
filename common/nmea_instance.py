from dataclasses import dataclass
from typing import Union
from common.nmea_data_types import GGA, RMC
from common.nmea_enum import Constellation, NMEAType


@dataclass
class NMEAInstance:
    def __init__(self, data):
        self.nmea_str = data
        try:
            self.constellation = Constellation[data[1:3]]
            self.type = NMEAType[data[3:6]]
        except KeyError:
            print(f"Invalid constellation or NMEA type in sentence: {data}")
            self.constellation = None
            self.type = None



    constellation: Constellation | None = None
    type: NMEAType | None= None
    nmea_str: str = None
    data: Union[GGA, RMC] = None

    def parse(self):
        if self.nmea_str is None:
            print("No valid data to construct instance!")
            return

        if self.type == NMEAType.GGA:
            from .nmea_parsers import GGA_parser
            GGA_parser(self)

        return