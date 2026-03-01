from common.nmea_data_manager import NMEAManager
from common.nmea_instance import NMEAInstance

path = r"data/ISTShuttle.nmea"

nmea_instances: NMEAManager = NMEAManager()

with open(path, "r", encoding="utf-8") as f:
    for line in f:
        instance = NMEAInstance(line)
        nmea_instances.add_instance(instance)


    for instance in nmea_instances.get_instances():
        instance.parse()


    nmea_instances.print_status()