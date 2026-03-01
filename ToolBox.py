from collections import defaultdict
from typing import List, Dict

from common.nmea_enum import NMEAType
from common.nmea_instance import NMEAInstance

path = r"data/ISTShuttle.nmea"

nmea_instances: Dict[NMEAType, List[NMEAInstance]] = defaultdict(list)

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        instance = NMEAInstance(line)
        nmea_instances[instance.type].append(instance)

    for key in nmea_instances.keys():
        print(f"{key}: {len(nmea_instances[key])} instances")