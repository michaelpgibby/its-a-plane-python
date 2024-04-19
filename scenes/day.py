from datetime import datetime

from utilities.animator import Animator
from setup import colours, fonts, frames
from setup.colours import COLORS
from config import DAY_COLOR

from rgbmatrix import graphics

# Setup
# DAY_COLOUR = colours.PINK_DARK
DAY_COLOUR = COLORS.get(DAY_COLOR, COLORS['WHITE'])
DAY_FONT = fonts.small
DAY_POSITION = (2, 23)


class DayScene(object):
    def __init__(self):
        super().__init__()
        self._last_day = None
        self._day_colour = COLORS.get(DAY_COLOR, COLORS['WHITE'])  # Added dynamic color attribute

    def set_day_color(self, color):
        self._day_colour = color

    @Animator.KeyFrame.add(frames.PER_SECOND * 1)
    def day(self, count):
        if len(self._data):
            # Ensure redraw when there's new data
            self._last_day = None

        else:
            # If there's no data to display
            # then draw the day
            now = datetime.now()
            current_day = now.strftime("%A")

            # Only draw if day needs updated
            if self._last_day != current_day:
                # Undraw last day if different from current
                if not self._last_day is None:
                    _ = graphics.DrawText(
                        self.canvas,
                        DAY_FONT,
                        DAY_POSITION[0],
                        DAY_POSITION[1],
                        COLORS["BLACK"],
                        self._last_day,
                    )
                self._last_day = current_day

                # Draw day with dynamically set color
                _ = graphics.DrawText(
                    self.canvas,
                    DAY_FONT,
                    DAY_POSITION[0],
                    DAY_POSITION[1],
                    self._day_colour,
                    current_day,
                )
