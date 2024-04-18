# config.py

import json
from setup import colours
from setup.colours import COLORS

# Load configuration from web_config.json
with open('web_config.json', 'r') as config_file:
    config_data = json.load(config_file)

COLORS_MAP = {
    "BLACK": colours.BLACK,
    "WHITE": colours.WHITE,
    "GREY": colours.GREY,
    "YELLOW": colours.YELLOW,
    "YELLOW_DARK": colours.YELLOW_DARK,
    "BLUE": colours.BLUE,
    "BLUE_LIGHT": colours.BLUE_LIGHT,
    "BLUE_DARK": colours.BLUE_DARK,
    "BLUE_DARKER": colours.BLUE_DARKER,
    "PINK": colours.PINK,
    "PINK_DARK": colours.PINK_DARK,
    "PINK_DARKER": colours.PINK_DARKER,
    "GREEN": colours.GREEN,
    "ORANGE": colours.ORANGE,
    "ORANGE_DARK": colours.ORANGE_DARK,
    "RED": colours.RED,
    "RED_LIGHT": colours.RED_LIGHT
}

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
AIRPORT_COLOR = COLORS_MAP.get(config_data['AIRPORT_COLOR'], colours.WHITE)
ARROW_COLOR = COLORS_MAP.get(config_data['ARROW_COLOR'], colours.WHITE)
PLANE_DETAILS_COLOR = COLORS_MAP.get(config_data['PLANE_DETAILS_COLOR'], colours.WHITE)
