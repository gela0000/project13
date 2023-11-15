"""
File: bouncing_ball.py
Name:Angela
-------------------------
TODO: This program bounces the ball three times and sets the ball back to its starting point.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    while True:
        ball.filled = True
        window.add(ball, x=START_X, y=START_Y)
        onmouseclicked(bounce)
        pause(DELAY)


def bounce(mouse):
    global count
    if ball.x == START_X and ball.y == START_Y and count < 3:
        count += 1
        while ball.x + SIZE/2 < 800:
            vy = 0
            while ball.y + SIZE/2 < 500:
                ball.x += VX
                ball.y += vy
                vy += GRAVITY
                pause(DELAY)
            vy = -vy * REDUCE
            while vy < 0:
                ball.x += VX
                ball.y += vy
                vy += GRAVITY
                pause(DELAY)


if __name__ == "__main__":
    main()
