from enum import Enum

class UAVState(Enum):
    IN_AIR = 1
    LANDED = 2
    TAKING_OFF = 3
    UNKNOWN = 4

# Locate the aircraft to specified point
def locate(latitude, longitude, altitude):
    return

# Locate with same altitude
def locate(latitude, longitude):
    return

# Accelerate the aircraft
def gain_speed(speed):
    return

# Starts takeoff
def takeof():
    return

# Prepare landing gears etc
def prepare_landing():
    return

# Starts landing
def land():
    return

# Checks if the aircraft is in the air
def is_in_air():
    return False # Stub

# Gets the current state of the UAV
def get_state():
    return UAVState.UNKNOWN