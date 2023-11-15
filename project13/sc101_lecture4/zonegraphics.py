from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:

    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.w = GWindow(window_width, window_height)
        # Create zone
        self.zone = GRect(zone_width, zone_height)
        self.w.add(self.zone, x=(window_width-zone_width)/2, y=(window_height-zone_height)/2)
        # Create ball and initialize velocity/position
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.w.add(self.ball)

        self.set_ball_position()

    def set_ball_position(self):
        random_x = random.randint(0, self.w.width-self.ball.width)
        random_y = random.randint(0, self.w.height - self.ball.height)
        self.ball.x = random_x
        self.ball.y = random_y
        # Initialize mouse listeners

        pass
