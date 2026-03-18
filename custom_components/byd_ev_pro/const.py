"""Constants for BYD EV Pro integration."""

DOMAIN = "byd_ev_pro"
MANUFACTURER = "BYD"

# Sensor definitions: (key_in_payload, name, device_class, unit, state_class, icon)
# device_class: https://developers.home-assistant.io/docs/core/entity/sensor/#available-device-classes
# state_class: "measurement" for instantaneous, "total_increasing" for monotonic counters
SENSOR_DEFINITIONS: list[tuple[str, str, str | None, str | None, str | None, str | None]] = [
    # Battery
    ("battery_soc", "Battery Level", "battery", "%", "measurement", None),
    ("battery_health", "Battery Health", None, "%", "measurement", "mdi:battery-heart-variant"),
    ("battery_voltage", "HV Battery Voltage", "voltage", "V", "measurement", None),
    ("battery_current", "HV Battery Current", "current", "A", "measurement", None),
    ("battery_power", "Battery Power", "power", "kW", "measurement", None),
    ("aux_voltage", "12V Battery", "voltage", "V", "measurement", None),
    ("cell_max_voltage", "Cell Max Voltage", "voltage", "V", "measurement", None),
    ("cell_min_voltage", "Cell Min Voltage", "voltage", "V", "measurement", None),
    # Temperature
    ("cabin_temp", "Cabin Temperature", "temperature", "\u00b0C", "measurement", None),
    ("outside_temp", "Outside Temperature", "temperature", "\u00b0C", "measurement", None),
    ("battery_max_temp", "Battery Max Temperature", "temperature", "\u00b0C", "measurement", None),
    ("battery_min_temp", "Battery Min Temperature", "temperature", "\u00b0C", "measurement", None),
    ("front_motor_temp", "Front Motor Temperature", "temperature", "\u00b0C", "measurement", None),
    # Driving
    ("range", "EV Range", "distance", "km", "measurement", None),
    ("odometer", "Odometer", "distance", "km", "total_increasing", None),
    ("speed", "Speed", "speed", "km/h", "measurement", None),
    ("vehicle_state", "Vehicle State", None, None, None, "mdi:car"),
    # Charging
    ("charging_state", "Charging State", None, None, None, "mdi:ev-station"),
    ("charging_gun", "Charging Gun", None, None, None, "mdi:ev-plug-type2"),
    # Climate
    ("ac_power", "Climate", None, None, None, "mdi:air-conditioner"),
    ("driver_temp_set", "Driver Temperature Setting", "temperature", "\u00b0C", "measurement", None),
    ("fan_speed", "Fan Speed", None, None, None, "mdi:fan"),
    # Other
    ("steering_heat", "Steering Wheel Heat", None, None, None, "mdi:steering"),
    ("driver_seat_heat", "Driver Seat Heat", None, None, None, "mdi:car-seat-heater"),
    ("front_motor_rpm", "Front Motor Speed", None, "RPM", "measurement", "mdi:engine"),
]

# Human-readable state mappings
VEHICLE_STATE_MAP = {0: "OFF", 1: "ACC", 2: "READY"}
CHARGING_STATE_MAP = {0: "Not Charging", 1: "Charging", 2: "Charge Complete"}
GUN_STATE_MAP = {0: "Disconnected", 1: "Connected (idle)", 2: "Connected (charging)"}
AC_POWER_MAP = {0: "Off", 1: "On"}
