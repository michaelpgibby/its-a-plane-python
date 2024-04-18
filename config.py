# config.py

import json
from setup import colours

# Load configuration from web_config.json
with open('web_config.json', 'r') as config_file:
    config_data = json.load(config_file)

ZONE_HOME = config_data['ZONE_HOME']
LOCATION_HOME = config_data['LOCATION_HOME']
WEATHER_LOCATION = config_data['WEATHER_LOCATION']
OPENWEATHER_API_KEY = config_data['OPENWEATHER_API_KEY']
TEMPERATURE_UNITS = config_data['TEMPERATURE_UNITS']
MIN_ALTITUDE = config_data['MIN_ALTITUDE']
BRIGHTNESS = config_data['BRIGHTNESS']
GPIO_SLOWDOWN = config_data['GPIO_SLOWDOWN']
JOURNEY_CODE_SELECTED = config_data['JOURNEY_CODE_SELECTED']
JOURNEY_BLANK_FILLER = config_data['JOURNEY_BLANK_FILLER']
HAT_PWM_ENABLED = config_data['HAT_PWM_ENABLED']
AIRPORT_COLOR = colours.get(config_data['AIRPORT_COLOR'], colours.BLACK)
ARROW_COLOR = colours.get(config_data['ARROW_COLOR'], colours.BLACK)
PLANE_DETAILS_COLOR = colours.get(config_data['PLANE_DETAILS_COLOR'], colours.BLACK)