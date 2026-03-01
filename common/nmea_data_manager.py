from collections import defaultdict
from typing import Dict, List

from ToolBox import nmea_instances
from common.nmea_enum import NMEAType
from common.nmea_instance import NMEAInstance


class NMEAManager:
    nmea_instances: Dict[NMEAType, List[NMEAInstance]] = defaultdict(list)

    def filter(self, condition):
        nmea_instances