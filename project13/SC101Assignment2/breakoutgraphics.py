"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This program provides the graphics and
functions for breakout.py.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 4    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)//2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius*2)//2, y=(window_height-ball_radius*2)//2)
        self.ball.filled = True
        self.window.add(self.ball)

        # scoreboard
        self.scoreboard = GLabel("Score: 0")
        self.scoreboard.font = "-30"
        self.window.add(self.scoreboard, x=self.window.width-self.scoreboard.width, y=50)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.move_with_mouse)
        onmouseclicked(self.ball_move)

        # Draw bricks
        color = "Red"
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                brick = GRect(brick_width, brick_height, x=(brick_width+brick_spacing)*i, y=brick_offset+(brick_height+brick_spacing)*j)
                self.window.add(brick)
                brick.filled = True
                if j == 0 or j == 1:
                    color = "Red"
                elif j == 2 or j == 3:
                    color = "Orange"
                elif j == 4 or j == 5:
                    color = "Yellow"
                elif j == 6 or j == 7:
                    color = "Green"
                elif j == 8 or j == 9:
                    color = "Blue"
                brick.fill_color = color

    def move_with_mouse(self, event):
        if 0 <= event.x - self.paddle.width/2 <= self.window.width-self.paddle.width:  # paddle in window
            self.paddle.x = event.x - self.paddle.width/2

    def ball_move(self, event):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset(self):
        self.window.add(self.ball, x=(self.window.width-self.ball.width)//2, y=(self.window.height-self.ball.height)//2)
        self.__dx = 0
        self.__dy = 0

    @staticmethod
    def get_brick_num():
        return BRICK_ROWS * BRICK_COLS

    def failed(self):
        fail = GLabel("Game Over.")
        self.window.add(fail, x=(self.window.width - fail.width) // 2, y=(self.window.height - fail.height) // 2 + 150)

    def success(self):
        congrats = GLabel("Congratulation!")
        self.window.add(congrats, x=(self.window.width-congrats.width)//2, y = (self.window.height-congrats.height)//2 + 150)

