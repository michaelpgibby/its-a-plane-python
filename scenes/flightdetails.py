from utilities.animator import Animator
from setup import colours, fonts, screen
from setup.colours import COLORS
from config import (
    FLIGHT_NUMBER_ALPHA_COLOR,
    FLIGHT_NUMBER_NUMERIC_COLOR,
    DIVIDING_BAR_COLOR,
    DATA_INDEX_COLOR,
)

from rgbmatrix import graphics

# Setup
BAR_STARTING_POSITION = (0, 18)
BAR_PADDING = 2

FLIGHT_NO_POSITION = (1, 21)
FLIGHT_NO_TEXT_HEIGHT = 8  # based on font size
FLIGHT_NO_FONT = fonts.small

# FLIGHT_NUMBER_ALPHA_COLOUR = colours.BLUE
# FLIGHT_NUMBER_NUMERIC_COLOUR = colours.BLUE_LIGHT

FLIGHT_NUMBER_ALPHA_COLOUR = COLORS.get(FLIGHT_NUMBER_ALPHA_COLOR, COLORS["WHITE"])
FLIGHT_NUMBER_NUMERIC_COLOUR = COLORS.get(
    FLIGHT_NUMBER_NUMERIC_COLOR, COLORS["WHITE"]
)

DATA_INDEX_POSITION = (52, 21)
DATA_INDEX_TEXT_HEIGHT = 6
DATA_INDEX_FONT = fonts.extrasmall

# DIVIDING_BAR_COLOUR = colours.GREEN
# DATA_INDEX_COLOUR = colours.GREY

DIVIDING_BAR_COLOUR = COLORS.get(DIVIDING_BAR_COLOR, COLORS["BLUE"])
DATA_INDEX_COLOUR = COLORS.get(DATA_INDEX_COLOR, COLORS["GREY"])


class FlightDetailsScene(object):
    def __init__(self):
        super().__init__()
        self._flight_number_alpha_colour = COLORS.get(
            FLIGHT_NUMBER_ALPHA_COLOR, COLORS["WHITE"]
        )
        self._flight_number_numeric_colour = COLORS.get(
            FLIGHT_NUMBER_NUMERIC_COLOR, COLORS["WHITE"]
        )
        self._dividing_bar_colour = COLORS.get(DIVIDING_BAR_COLOR, COLORS["BLUE"])
        self._data_index_colour = COLORS.get(DATA_INDEX_COLOR, COLORS["GREY"])

    def set_flight_details_colors(
        self,
        flight_number_alpha_colour,
        flight_number_numeric_colour,
        dividing_bar_colour,
        data_index_colour,
    ):
        self._flight_number_alpha_colour = flight_number_alpha_colour
        self._flight_number_numeric_colour = flight_number_numeric_colour
        self._dividing_bar_colour = dividing_bar_colour
        self._data_index_colour = data_index_colour

    @Animator.KeyFrame.add(0)
    def flight_details(self):
        # Guard against no data
        if len(self._data) == 0:
            return

        # Clear the whole area
        self.draw_square(
            0,
            BAR_STARTING_POSITION[1] - (FLIGHT_NO_TEXT_HEIGHT // 2),
            screen.WIDTH - 1,
            BAR_STARTING_POSITION[1] + (FLIGHT_NO_TEXT_HEIGHT // 2),
            COLORS["BLACK"],
        )

        # Draw flight number if available
        flight_no_text_length = 0
        if (
            self._data[self._data_index]["callsign"]
            and self._data[self._data_index]["callsign"] != "N/A"
        ):
            flight_no = f'{self._data[self._data_index]["callsign"]}'

            for ch in flight_no:
                ch_length = graphics.DrawText(
                    self.canvas,
                    FLIGHT_NO_FONT,
                    FLIGHT_NO_POSITION[0] + flight_no_text_length,
                    FLIGHT_NO_POSITION[1],
                    self._flight_number_numeric_colour
                    if ch.isnumeric()
                    else self._flight_number_alpha_colour,
                    ch,
                )
                flight_no_text_length += ch_length

        # Draw bar
        if len(self._data) > 1:
            # Clear area where N of M might have been
            self.draw_square(
                DATA_INDEX_POSITION[0] - BAR_PADDING,
                BAR_STARTING_POSITION[1] - (FLIGHT_NO_TEXT_HEIGHT // 2),
                screen.WIDTH,
                BAR_STARTING_POSITION[1] + (FLIGHT_NO_TEXT_HEIGHT // 2),
                COLORS["BLACK"],
            )

            # Dividing bar
            graphics.DrawLine(
                self.canvas,
                flight_no_text_length + BAR_PADDING,
                BAR_STARTING_POSITION[1],
                DATA_INDEX_POSITION[0] - BAR_PADDING - 1,
                BAR_STARTING_POSITION[1],
                self._dividing_bar_colour,
            )

            # Draw text
            text_length = graphics.DrawText(
                self.canvas,
                fonts.extrasmall,
                DATA_INDEX_POSITION[0],
                DATA_INDEX_POSITION[1],
                self._data_index_colour,
                f"{self._data_index + 1}/{len(self._data)}",
            )
        else:
            # Dividing bar
            graphics.DrawLine(
                self.canvas,
                flight_no_text_length + BAR_PADDING if flight_no_text_length else 0,
                BAR_STARTING_POSITION[1],
                screen.WIDTH,
                BAR_STARTING_POSITION[1],
                self._dividing_bar_colour,
            )

