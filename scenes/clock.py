from datetime import datetime

from utilities.animator import Animator
from setup import colours, fonts, frames
from setup.colours import COLORS

from config import CLOCK_COLOR

from rgbmatrix import graphics

# Setup
CLOCK_FONT = fonts.regular
CLOCK_POSITION = (1, 8)
# CLOCK_COLOUR = colours.BLUE_DARK
# Update: Use CLOCK_COLOR from config instead of hardcoding
CLOCK_COLOUR = COLORS.get(CLOCK_COLOR, COLORS['WHITE'])
print(f"CLOCK_COLOR: {CLOCK_COLOR}")

class ClockScene(object):
    def __init__(self):
        super().__init__()
        self._last_time = None

    def set_clock_color(self, color):
        # Update: Method to set the clock color
        self._clock_colour = color

    @Animator.KeyFrame.add(frames.PER_SECOND * 1)
    def clock(self, count):
        if len(self._data):
            # Ensure redraw when there's new data
            self._last_time = None

        else:
            # If there's no data to display
            # then draw a clock
            now = datetime.now()
            current_time = now.strftime("%H:%M")

            # Only draw if time needs updating
            if self._last_time != current_time:
                # Undraw last time if different from current
                if self._last_time is not None:
                    _ = graphics.DrawText(
                        self.canvas,
                        CLOCK_FONT,
                        CLOCK_POSITION[0],
                        CLOCK_POSITION[1],
                        COLORS["BLACK"],
                        self._last_time,
                    )
                self._last_time = current_time

                # Draw Time using updated CLOCK_COLOUR
                _ = graphics.DrawText(
                    self.canvas,
                    CLOCK_FONT,
                    CLOCK_POSITION[0],
                    CLOCK_POSITION[1],
                    self._clock_colour,  # Updated to use self._clock_colour
                    current_time,
                )
