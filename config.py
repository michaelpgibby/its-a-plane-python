# config.py

import json
from setup import colours
from setup.colours import COLORS


# Load configuration from web_config.json
with open('web_config.json', 'r') as config_file:
    config_data = json.load(config_file)

COLORS_MAP = {
    "BLACK": COLORS["BLACK"],
"WHITE": COLORS["WHITE"],
"GREY": COLORS["GREY"],
"YELLOW": COLORS["YELLOW"],
"YELLOW_DARK": COLORS["YELLOW_DARK"],
"BLUE": COLORS["BLUE"],
"BLUE_LIGHT": COLORS["BLUE_LIGHT"],
"BLUE_DARK": COLORS["BLUE_DARK"],
"BLUE_DARKER": COLORS["BLUE_DARKER"],
"PINK": COLORS["PINK"],
"PINK_DARK": COLORS["PINK_DARK"],
"PINK_DARKER": COLORS["PINK_DARKER"],
"GREEN": COLORS["GREEN"],
"ORANGE": COLORS["ORANGE"],
"ORANGE_DARK": COLORS["ORANGE_DARK"],
"RED": COLORS["RED"],
"RED_LIGHT": COLORS["RED_LIGHT"]

}

ZONE_HOME = {
    "tl_y": config_data['ZONE_HOME_tl_y'], # Top-Left Latitude (deg)
    "tl_x": config_data['ZONE_HOME_tl_x'], # Top-Left Longitude (deg)
    "br_y": config_data['ZONE_HOME_br_y'], # Bottom-Right Latitude (deg)
    "br_x": config_data['ZONE_HOME_br_x'] # Bottom-Right Longitude (deg)
}
LOCATION_HOME = [
    config_data['LOCATION_HOME_latitude'], # Latitude (deg)
    config_data['LOCATION_HOME_longitude'], # Longitude (deg)
    config_data['LOCATION_HOME_altitude'] # Altitude (km)
]
WEATHER_LOCATION = config_data['WEATHER_LOCATION']
OPENWEATHER_API_KEY = config_data['OPENWEATHER_API_KEY']
# TEMPERATURE_UNITS = config_data['TEMPERATURE_UNITS']
MIN_ALTITUDE = config_data['MIN_ALTITUDE']
BRIGHTNESS = config_data['BRIGHTNESS']
GPIO_SLOWDOWN = config_data['GPIO_SLOWDOWN']
JOURNEY_CODE_SELECTED = config_data['JOURNEY_CODE_SELECTED']
JOURNEY_BLANK_FILLER = config_data['JOURNEY_BLANK_FILLER']
HAT_PWM_ENABLED = config_data['HAT_PWM_ENABLED']
AIRPORT_COLOR = COLORS_MAP.get(config_data['AIRPORT_COLOR'], COLORS["YELLOW"])
ARROW_COLOR = COLORS_MAP.get(config_data['ARROW_COLOR'], COLORS["ORANGE"])
PLANE_DETAILS_COLOR = COLORS_MAP.get(config_data['PLANE_DETAILS_COLOR'], COLORS["PINK"])
CLOCK_COLOR = COLORS_MAP.get(config_data['CLOCK_COLOR'], COLORS["WHITE"])
DATE_COLOR = COLORS_MAP.get(config_data['DATE_COLOR'], COLORS["WHITE"])
DAY_COLOR = COLORS_MAP.get(config_data['DAY_COLOR'], COLORS["WHITE"])
FLIGHT_NUMBER_ALPHA_COLOR = COLORS_MAP.get(config_data['FLIGHT_NUMBER_ALPHA_COLOR'], COLORS["BLUE_LIGHT"])
FLIGHT_NUMBER_NUMERIC_COLOR = COLORS_MAP.get(config_data['FLIGHT_NUMBER_NUMERIC_COLOR'], COLORS["BLUE_DARK"])
DIVIDING_BAR_COLOR = COLORS.get(config_data['DIVIDING_BAR_COLOR'], COLORS["BLUE"])
DATA_INDEX_COLOR = COLORS.get(config_data['DATA_INDEX_COLOR'], COLORS["GREY"])
JOURNEY_COLOR = COLORS.get(config_data['JOURNEY_COLOR'], COLORS["YELLOW"])
RGB_SEQUENCE = config_data.get('RGB_SEQUENCE', "RGB")

RAINFALL_ENABLED = config_data.get('RAINFALL_ENABLED', False)
RAINFALL_HOURS = config_data.get('RAINFALL_HOURS', 24)
RAINFALL_OVERSPILL_FLASH_ENABLED = config_data.get('RAINFALL_OVERSPILL_FLASH_ENABLED', True)
RAINFAILL_12HR_MARKERS = True
RAINFALL_GRAPH_ORIGIN = (39, 15)
RAINFALL_COLUMN_WIDTH = 1
RAINFALL_GRAPH_HEIGHT = 8
RAINFALL_MAX_VALUE = 3
RAINFALL_REFRESH_SECONDS = 60
TEMPERATURE_FONT_HEIGHT =  5
TEMPERATURE_POSITION = (48, TEMPERATURE_FONT_HEIGHT + 1)
