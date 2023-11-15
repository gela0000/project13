"""
File: my_drawing.py
Name: 
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=800, height=500, title="train")

    label = GLabel("Hi!")
    window.add(label, x=375, y=150)
    label.font = "-50"

    l_body = GRect(150, 100, x=200, y=250)
    window.add(l_body)
    l_body.filled = True
    l_body.fill_color = "tomato"

    lu_body = GRect(180, 20, x=185, y=230)
    window.add(lu_body)
    lu_body.filled = True
    lu_body.fill_color = "sage"

    connection = GRect(30, 20, x=350, y=315)
    window.add(connection)
    connection.filled = True
    connection.fill_color = "saddlebrown"

    r_body = GRect(100, 130, x=380, y=220)
    window.add(r_body)
    r_body.filled = True
    r_body.fill_color = "seagreen"

    ru_body = GRect(130, 20, x=365, y=200)
    window.add(ru_body)
    ru_body.filled = True
    ru_body.fill_color = "red"

    head = GRect(90, 70, x=480, y=280)
    window.add(head)
    head.filled = True
    head.fill_color = "sage"

    wheel_1 = GOval(40, 40, x=210, y=350)
    window.add(wheel_1)
    wheel_1.filled = True
    wheel_1.fill_color = "brown"

    wheel_2 = GOval(40, 40, x=290, y=350)
    window.add(wheel_2)
    wheel_2.filled = True
    wheel_2.fill_color = "brown"

    wheel_3 = GOval(40, 40, x=390, y=350)
    window.add(wheel_3)
    wheel_3.filled = True
    wheel_3.fill_color = "brown"

    wheel_4 = GOval(40, 40, x=450, y=350)
    window.add(wheel_4)
    wheel_4.filled = True
    wheel_4.fill_color = "brown"

    wheel_5 = GOval(40, 40, x=510, y=350)
    window.add(wheel_5)
    wheel_5.filled = True
    wheel_5.fill_color = "brown"




if __name__ == '__main__':
    main()
