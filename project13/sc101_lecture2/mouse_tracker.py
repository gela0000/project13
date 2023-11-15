"""
File: mouse_tracker.py
Name:
------------------------
This file shows how to use campy
mouse event to draw GOval
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmousemoved, onmouseclicked, onmousedragged

# This constant controls the size of the GRect
SIZE = 30
window = GWindow()
rect = GRect(SIZE, SIZE)


def main():
	onmousemoved(move)
	onmouseclicked(draw)
	onmousedragged(draw)
	rect.filled = True
	window.add(rect)


def move(moved_mouse):
	rect.x = moved_mouse.x - SIZE//2
	rect.y = moved_mouse.y - SIZE//2


def draw(mouse):
	stroke = GRect(SIZE, SIZE)
	stroke.filled = True
	window.add(stroke, x=mouse.x-SIZE//2, y=mouse.y-SIZE//2)


if __name__ == '__main__':
	main()
