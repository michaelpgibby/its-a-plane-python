from animator import Animator
from constants import framerate, colours, fonts

from rgbmatrix import graphics

JOURNEY_POSITION = (0, 0)
JOURNEY_HEIGHT = 12
JOURNEY_WIDTH = 64
JOURNEY_SPACING = 16
JOURNEY_FONT = fonts.fonts_large
JOURNEY_FONT_SELECTED = fonts.fonts_large_bold
JOURNEY_CODE_SELECTED = "GLA"
JOURNEY_BLANK_FILLER = "UFO"

JOURNEY_COLOUR = colours.COLOUR_YELLOW

ARROW_COLOUR = colours.COLOUR_ORANGE

# Element Positions
ARROW_POINT_POSITION = (34, 7)
ARROW_WIDTH = 4
ARROW_HEIGHT = 8


class JourneyScene:
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
            colours.COLOUR_BLACK,
        )

        # Draw origin
        text_length = graphics.DrawText(
            self.canvas,
            JOURNEY_FONT_SELECTED if origin == JOURNEY_CODE_SELECTED else JOURNEY_FONT,
            1,
            JOURNEY_HEIGHT,
            JOURNEY_COLOUR,
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
            JOURNEY_COLOUR,
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
            colours.COLOUR_BLACK,
        )

        # Starting positions for filled in arrow
        x = ARROW_POINT_POSITION[0] - ARROW_WIDTH
        y1 = ARROW_POINT_POSITION[1] - (ARROW_HEIGHT // 2)
        y2 = ARROW_POINT_POSITION[1] + (ARROW_HEIGHT // 2)

        # Tip of arrow
        self.canvas.SetPixel(
            ARROW_POINT_POSITION[0],
            ARROW_POINT_POSITION[1],
            ARROW_COLOUR.red,
            ARROW_COLOUR.green,
            ARROW_COLOUR.blue,
        )

        # Draw using columns
        for col in range(0, ARROW_WIDTH):
            graphics.DrawLine(
                self.canvas,
                x,
                y1,
                x,
                y2,
                ARROW_COLOUR,
            )

            # Calculate next column's data
            x += 1
            y1 += 1
            y2 -= 1