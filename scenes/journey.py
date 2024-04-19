from utilities.animator import Animator
from setup import colours, fonts
from setup.colours import COLORS
from config import JOURNEY_COLOR, ARROW_COLOR

from rgbmatrix import graphics

# Attempt to load config data
try:
    from config import JOURNEY_CODE_SELECTED

except (ModuleNotFoundError, NameError, ImportError):
    # If there's no config data
    JOURNEY_CODE_SELECTED = "GLA"

try:
    from config import JOURNEY_BLANK_FILLER

except (ModuleNotFoundError, NameError, ImportError):
    # If there's no config data
    JOURNEY_BLANK_FILLER = " ? "

# Setup
JOURNEY_POSITION = (0, 0)
JOURNEY_HEIGHT = 12
JOURNEY_WIDTH = 64
JOURNEY_SPACING = 16
JOURNEY_FONT = fonts.large
JOURNEY_FONT_SELECTED = fonts.large_bold
# JOURNEY_COLOUR = colours.YELLOW
# ARROW_COLOUR = colours.ORANGE

JOURNEY_COLOUR = COLORS.get(JOURNEY_COLOR, COLORS["YELLOW"])
ARROW_COLOUR = COLORS.get(ARROW_COLOR, COLORS["ORANGE"])

# Element Positions
ARROW_POINT_POSITION = (34, 7)
ARROW_WIDTH = 4
ARROW_HEIGHT = 8


class JourneyScene(object):
    def __init__(self):
        super().__init__()
        self._journey_colour = COLORS.get(JOURNEY_COLOR, COLORS["YELLOW"])
        self._arrow_colour = COLORS.get(ARROW_COLOR, COLORS["ORANGE"])

    def set_journey_colors(self, journey_colour, arrow_colour):
        self._journey_colour = journey_colour
        self._arrow_colour = arrow_colour

    @Animator.KeyFrame.add(0)
    def journey(self):
        # Guard against no data
        if len(self._data) == 0:
            return

        origin = self._data[self._data_index]["origin"]
        destination = self._data[self._data_index]["destination"]

        # Draw background
        self.draw_square(
            JOURNEY_POSITION[0],
            JOURNEY_POSITION[1],
            JOURNEY_POSITION[0] + JOURNEY_WIDTH - 1,
            JOURNEY_POSITION[1] + JOURNEY_HEIGHT - 1,
            COLORS["BLACK"],
        )

        # Draw origin
        text_length = graphics.DrawText(
            self.canvas,
            JOURNEY_FONT_SELECTED if origin == JOURNEY_CODE_SELECTED else JOURNEY_FONT,
            1,
            JOURNEY_HEIGHT,
            self._journey_colour,
            origin if origin else JOURNEY_BLANK_FILLER,
        )

        # Draw destination
        _ = graphics.DrawText(
            self.canvas,
            JOURNEY_FONT_SELECTED
            if destination == JOURNEY_CODE_SELECTED
            else JOURNEY_FONT,
            text_length + JOURNEY_SPACING,
            JOURNEY_HEIGHT,
            self._journey_colour,
            destination if destination else JOURNEY_BLANK_FILLER,
        )

    @Animator.KeyFrame.add(0)
    def journey_arrow(self):
        # Guard against no data
        if len(self._data) == 0:
            return

        # Black area before arrow
        self.draw_square(
            ARROW_POINT_POSITION[0] - ARROW_WIDTH,
            ARROW_POINT_POSITION[1] - (ARROW_HEIGHT // 2),
            ARROW_POINT_POSITION[0],
            ARROW_POINT_POSITION[1] + (ARROW_HEIGHT // 2),
            COLORS["BLACK"],
        )

        # Starting positions for filled-in arrow
        x = ARROW_POINT_POSITION[0] - ARROW_WIDTH
        y1 = ARROW_POINT_POSITION[1] - (ARROW_HEIGHT // 2)
        y2 = ARROW_POINT_POSITION[1] + (ARROW_HEIGHT // 2)

        # Tip of arrow
        self.canvas.SetPixel(
            ARROW_POINT_POSITION[0],
            ARROW_POINT_POSITION[1],
            self._arrow_colour.red,
            self._arrow_colour.green,
            self._arrow_colour.blue,
        )

        # Draw using columns
        for col in range(0, ARROW_WIDTH):
            graphics.DrawLine(
                self.canvas,
                x,
                y1,
                x,
                y2,
                self._arrow_colour,
            )

            # Calculate next column's data
            x += 1
            y1 += 1
            y2 -= 1

