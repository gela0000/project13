"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program starts with a ball at the
center of a window with bricks on the top
and a paddle at the bottom. The ball
bounces off the paddle, the bricks, and
the window boarders. Destroy every brick
and you win, fall over the bottom window
boarder three times and you lose.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    death_count = 0
    brick_count = 0
    brick_num = graphics.get_brick_num()

    # get ball initial speed until mouse clicked
    while brick_count < 2:
        vx = graphics.get_dx()
        vy = graphics.get_dy()
        if vx != 0 and vy != 0:
            break
        pause(FRAME_RATE)

    # Animation loop
    while brick_count < brick_num:
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            vx = -vx
        if graphics.ball.y <= 0:
            vy = -vy
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.reset()
            if death_count < NUM_LIVES-1:
                death_count += 1
                while True:
                    vx = graphics.get_dx()
                    vy = graphics.get_dy()
                    if vx != 0 and vy != 0:
                        break
                    pause(FRAME_RATE)
            else:
                graphics.failed()
                break
        graphics.ball.move(vx, vy)

        obj_lt = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        obj_rt = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        obj_lb = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        obj_rb = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height)

        # Check for Collisions
        for obj in obj_lt, obj_rt, obj_lb, obj_rb:
            if obj is not None:
                if obj is graphics.paddle:
                    vy = -vy
                else:  # collide with brick
                    vy = -vy
                    graphics.window.remove(obj)
                    brick_count += 1
                    graphics.scoreboard.text = f"Score: {brick_count}"
                    graphics.scoreboard.x = graphics.window.width - graphics.scoreboard.width
                break

        pause(FRAME_RATE)

    if brick_count == brick_num:  # all bricks destroyed
        graphics.reset()
        graphics.success()


if __name__ == '__main__':
    main()
