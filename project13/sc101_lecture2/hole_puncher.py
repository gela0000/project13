"""
File: hole_puncher.py
Name:
------------------------
This file shows how to use campy
mouse event to punch holes (GOval)
on GWindow
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 20
window = GWindow()

def main():
	onmouseclicked(punch)


def punch(clicked_mouse):
	hole = GOval(SIZE, SIZE, x=clicked_mouse.x, y=clicked_mouse.y)
	hole.filled = True
	window.add(hole)



if __name__ == '__main__':
	main()
