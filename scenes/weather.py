import urllib.request
import datetime
import time
import json
from math import ceil
from functools import lru_cache
from rgbmatrix import graphics
from utilities.animator import Animator
from setup import colours, fonts, frames
from setup.colours import COLORS
from config import (
    WEATHER_LOCATION,
    OPENWEATHER_API_KEY,
    RAINFALL_ENABLED,
    RAINFALL_HOURS,
    RAINFAILL_12HR_MARKERS,
    RAINFALL_GRAPH_ORIGIN,
    RAINFALL_COLUMN_WIDTH,
    RAINFALL_GRAPH_HEIGHT,
    RAINFALL_MAX_VALUE,
    RAINFALL_OVERSPILL_FLASH_ENABLED
)

TEMPERATURE_COLOURS = (
    (0, COLORS['WHITE']),
    (1, COLORS['BLUE_LIGHT']),
    (8, COLORS['PINK_DARK']),
    (18, COLORS['YELLOW']),
    (30, COLORS['ORANGE']),
)

RAINFALL_12HR_MARKERS = True
RAINFALL_GRAPH_ORIGIN = (39, 15)
RAINFALL_COLUMN_WIDTH = 1
RAINFALL_GRAPH_HEIGHT = 8
RAINFALL_MAX_VALUE = 3
TEMPERATURE_FONT_HEIGHT = 5
TEMPERATURE_POSITION = (44, TEMPERATURE_FONT_HEIGHT + 1)
RAINFALL_REFRESH_SECONDS = 380
TEMPERATURE_REFRESH_SECONDS = 60
RAINFALL_HOURS = 24
RAINFALL_OVERSPILL_FLASH_ENABLED = True
TEMPERATURE_UNITS = 'metric'  # Set to 'metric' for Celsius

# Weather API
WEATHER_API_URL = "https://taps-aff.co.uk/api/"
OPENWEATHER_API_URL = "https://api.openweathermap.org/data/2.5/"

TEMPERATURE_FONT = fonts.small

# Cache grabbing weather data
@lru_cache()
def grab_weather(location, ttl_hash=None):
    del ttl_hash  # to emphasize we don't use

    request = urllib.request.Request(WEATHER_API_URL + location)
    raw_data = urllib.request.urlopen(request).read()
    content = json.loads(raw_data.decode("utf-8"))

    return content


def get_ttl_hash(seconds=60):
    """Return the same value within `seconds` time period"""
    return round(time.time() / seconds)


def grab_current_temperature(location, units="metric"):
    current_temp = None

    try:
        weather = grab_weather(location, ttl_hash=get_ttl_hash())
        current_temp = weather["temp_c"]

    except:
        pass

    return current_temp


def grab_upcoming_rainfall_and_temperature(location, hours):
    up_coming_rainfall_and_temperature = None

    try:
        weather = grab_weather(location, ttl_hash=get_ttl_hash())

        # We want to parse the data to find the
        # rainfall from now for <hours>
        forecast_today = weather["forecast"][0]["hourly"]
        forecast_tomorrow = weather["forecast"][1]["hourly"]
        hourly_forecast = forecast_today + forecast_tomorrow

        hourly_data = [
            {
                "precip_mm": hour["precip_mm"],
                "temp_c": hour["temp_c"],
                "hour": hour["hour"],
            }
            for hour in hourly_forecast
        ]

        now = datetime.datetime.now()
        current_hour = now.hour
        up_coming_rainfall_and_temperature = hourly_data[
            current_hour : current_hour + hours
        ]

    except:
        pass

    return up_coming_rainfall_and_temperature


def grab_current_temperature_openweather(location, apikey, units):
    current_temp = None

    try:
        request = urllib.request.Request(
            OPENWEATHER_API_URL
            + "weather?q="
            + location
            + "&appid="
            + apikey
            + "&units="
            + units
        )
        raw_data = urllib.request.urlopen(request).read()
        content = json.loads(raw_data.decode("utf-8"))
        current_temp = content["main"]["temp"]

    except:
        pass

    return current_temp


class WeatherScene(object):
    def __init__(self):
        super().__init__()
        self._last_upcoming_rain_and_temp = None
        self._last_temperature_str_f = None
        self._last_temperature_str_c = None

    def colour_gradient(self, colour_A, colour_B, ratio):
        return graphics.Color(
            colour_A.red + ((colour_B.red - colour_A.red) * ratio),
            colour_A.green + ((colour_B.green - colour_A.green) * ratio),
            colour_A.blue + ((colour_B.blue - colour_A.blue) * ratio),
        )

    def temperature_to_colour(self, current_temperature):
        # Set some defaults
        min_temp = TEMPERATURE_COLOURS[0][0]
        max_temp = TEMPERATURE_COLOURS[1][0]
        min_temp_colour = TEMPERATURE_COLOURS[0][1]
        max_temp_colour = TEMPERATURE_COLOURS[1][1]

        # Search to find where in the current
        # temperature lies within the
        # defined colours
        for i in range(1, len(TEMPERATURE_COLOURS) - 1):
            if current_temperature > TEMPERATURE_COLOURS[i][0]:
                min_temp = TEMPERATURE_COLOURS[i][0]
                max_temp = TEMPERATURE_COLOURS[i + 1][0]
                min_temp_colour = TEMPERATURE_COLOURS[i][1]
                max_temp_colour = TEMPERATURE_COLOURS[i + 1][1]

        if current_temperature > max_temp:
            ratio = 1
        elif current_temperature > min_temp:
            ratio = (current_temperature - min_temp) / (max_temp - min_temp)
        else:
            ratio = 0

        temp_colour = self.colour_gradient(min_temp_colour, max_temp_colour, ratio)

        return temp_colour

    @Animator.KeyFrame.add(frames.PER_SECOND * 1)
    def temperature(self, count):
        if len(self._data):
            # Don't draw if there's plane data
            return

        if not (count % TEMPERATURE_REFRESH_SECONDS):
            if OPENWEATHER_API_KEY:
                self.current_temperature = grab_current_temperature_openweather(
                    WEATHER_LOCATION, OPENWEATHER_API_KEY, TEMPERATURE_UNITS
                )
            else:
                self.current_temperature = grab_current_temperature(
                    WEATHER_LOCATION, TEMPERATURE_UNITS
                )

        if self._last_temperature_str_f is not None:
            # Undraw old temperatures
            _ = graphics.DrawText(
                self.canvas,
                TEMPERATURE_FONT,
                TEMPERATURE_POSITION[0],
                TEMPERATURE_POSITION[1],
                COLORS["BLACK"],
                self._last_temperature_str_f,
            )
            _ = graphics.DrawText(
                self.canvas,
                TEMPERATURE_FONT,
                TEMPERATURE_POSITION[0],
                TEMPERATURE_POSITION[1] + TEMPERATURE_FONT_HEIGHT + 1,
                COLORS["BLACK"],
                self._last_temperature_str_c,
            )

        if self.current_temperature:
            temp_str_c = f"{round(self.current_temperature)}°C".rjust(4, " ")
            temp_str_f = f"{round((self.current_temperature * (9/5))) + 32}°F".rjust(4, " ")

            temp_colour = self.temperature_to_colour(self.current_temperature)

            # Draw temperature in Fahrenheit
            _ = graphics.DrawText(
                self.canvas,
                TEMPERATURE_FONT,
                TEMPERATURE_POSITION[0],
                TEMPERATURE_POSITION[1],
                temp_colour,
                temp_str_f,
            )

            # Draw temperature in Celsius
            _ = graphics.DrawText(
                self.canvas,
                TEMPERATURE_FONT,
                TEMPERATURE_POSITION[0],
                TEMPERATURE_POSITION[1] + TEMPERATURE_FONT_HEIGHT + 1,
                temp_colour,
                temp_str_c,
            )

            self._last_temperature_str_f = temp_str_f
            self._last_temperature_str_c = temp_str_c

    # Other methods here...
