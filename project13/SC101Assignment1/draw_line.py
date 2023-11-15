"""
File: draw_line.py
Name: Angela
-------------------------
TODO: This program draws a circle on odd clicks and a line that connects the previous click and the last click on even clicks.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 10
window = GWindow()
count = 0
mouse_x = 0
mouse_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    if count % 2 == 0:
        onmouseclicked(draw)


def draw(clicked_mouse):
    """
    Draw a circle with SIZE as radius where the mouse is clicked.
    """
    global count, mouse_x, mouse_y
    if count % 2 == 0:
        mouse_x = clicked_mouse.x
        mouse_y = clicked_mouse.y
        circle = GOval(2*SIZE, 2*SIZE, x=clicked_mouse.x-SIZE, y=clicked_mouse.y-SIZE)
        window.add(circle)
        count += 1
    else:
        circle = window.get_object_at(mouse_x, mouse_y)
        window.remove(circle)
        line = GLine(mouse_x, mouse_y, clicked_mouse.x, clicked_mouse.y)
        window.add(line)
        count += 1


if __name__ == "__main__":
    main()
