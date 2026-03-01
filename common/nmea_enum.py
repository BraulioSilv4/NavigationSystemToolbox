from enum import Enum


class NMEAType(Enum):
    GGA = "GGA"
    RMC = "RMC"
    GLL = "GLL"
    GSA = "GSA"
    GSV = "GSV"
    VTG = "VTG"
    ZDA = "ZDA"



class DistanceMeasureUnit(Enum):
    METERS  = 'M'
    FEET    = 'F'



class Constellation(Enum):
    GP      = "GPs"
    GL      = "GLONASS"
    GA      = "GALILEO"
    GN      = "GNSS"
    GB      = "BEIDOU_GB"
    BD      = "BEIDOU_BD"
    EP      = "EPIRB"



class FixQuality(Enum):
    INVALID         = 0
    GPS_FIX         = 1
    DGPS_SPS        = 2
    PPS             = 3
    RTK_INT         = 4
    RTK_FLOAT       = 5
    DEAD_RECKONING  = 6
    MANUAL_INPUT    = 7
    SIM_MODE        = 8



class Hemisphere(Enum):
    NORTH = 'N'
    SOUTH = 'S'
    EAST  = 'E'
    WEST  = 'W'


