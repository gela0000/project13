"""
File: whack_a_mole.py
Name: 
---------------------------
This program plays a game called
"whack a mole" in which players 
clicking the popping moles 
on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700

window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
score = 0
score_label = GLabel("Score: " + str(score))

def main():
    onmouseclicked(remove)
    score_label.font = "-40"
    window.add(score_label, x=0, y=score_label.height)
    while True:
        img = GImage('mole.png')
        random_x = random.randint(0, WINDOW_WIDTH-img.width)
        random_y = random.randint(0, WINDOW_HEIGHT-img.height)
        window.add(img, x=random_x, y=random_y)
        pause(DELAY)


def remove(clicked_mouse):
    global score, score_label
    maybe_obj = window.get_object_at(clicked_mouse.x, clicked_mouse.y)
    if maybe_obj is not None and maybe_obj is not score_label:
        window.remove(maybe_obj)
        score += 1
        score_label.text = "Score: " + str(score)


if __name__ == '__main__':
    main()
