from typing import List
from common.nmea_instance import NMEAInstance

path = r"data/ISTShuttle.nmea"

nmea_instances: List[NMEAInstance] = []

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        nmea_instances.append(NMEAInstance(line))

    for instance in nmea_instances:
        if instance.type == "GGA":
            instance.parse()

    for instance in nmea_instances:
        if instance.type == "GGA":
            print(instance.data)