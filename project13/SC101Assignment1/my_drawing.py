"""
File: my_drawing.py
Name:
----------------------
TODO: This program draws a cute hamster! :)
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Just last week, I passed by PetPark by chance. Since I really like animals, I thought to go in and get some AC along
    the way. The moment that I stepped in, my eyes met the eyes of a cute hamster and that night, it went home with me.
    Its name is 小泡芙 :)
    """
    window = GWindow(width=500, height=500, title="hamster")

    l_ear = GOval(50, 90, x=173, y=68)
    window.add(l_ear)
    l_ear.filled = True
    l_ear.fill_color = "#37260a"
    l_ear.color = "#edd1a2"

    r_ear = GOval(50, 90, x=273, y=68)
    window.add(r_ear)
    r_ear.filled = True
    r_ear.fill_color = "#37260a"
    r_ear.color = "#edd1a2"

    l_body = GOval(130, 200, x=140, y=170)
    window.add(l_body)
    l_body.filled = True
    l_body.fill_color = "#edd1a2"
    l_body.color = "#edd1a2"

    r_body = GOval(130, 200, x=230, y=170)
    window.add(r_body)
    r_body.filled = True
    r_body.fill_color = "#edd1a2"
    r_body.color = "#edd1a2"

    head = GOval(220, 145, x=140, y=100)
    window.add(head)
    head.filled = True
    head.fill_color = "#edd1a2"
    head.color = "#edd1a2"

    l_cheek = GOval(85, 70, x=125, y=150)
    window.add(l_cheek)
    l_cheek.filled = True
    l_cheek.fill_color = "#f2e3b8"
    l_cheek.color = "#edd1a2"

    r_cheek = GOval(95, 82, x=273, y=145)
    window.add(r_cheek)
    r_cheek.filled = True
    r_cheek.fill_color = "#f2e3b8"
    r_cheek.color = "#edd1a2"

    l_eye = GArc(30, 50, 20, 100)
    window.add(l_eye, x=200, y=140)

    r_eye = GArc(75, 65, 90, 75)
    window.add(r_eye, x=265, y=135)

    nose = GPolygon()
    nose.add_vertex((230, 165))
    nose.add_vertex((250, 165))
    nose.add_vertex((240, 182))
    nose.filled = True
    nose.fill_color = "pink"
    nose.color = "pink"
    window.add(nose)

    l_foot = GPolygon()
    l_foot.add_vertex((190, 365))
    l_foot.add_vertex((182, 385))
    l_foot.add_vertex((152, 385))
    l_foot.add_vertex((152, 375))
    l_foot.add_vertex((172, 368))
    l_foot.add_vertex((175, 361))
    l_foot.filled = True
    l_foot.fill_color = "pink"
    l_foot.color = "pink"
    window.add(l_foot)

    r_foot = GPolygon()
    r_foot.add_vertex((300, 370))
    r_foot.add_vertex((303, 385))
    r_foot.add_vertex((330, 385))
    r_foot.add_vertex((328, 370))
    r_foot.add_vertex((320, 368))
    r_foot.add_vertex((318, 363))
    r_foot.filled = True
    r_foot.fill_color = "pink"
    r_foot.color = "pink"
    window.add(r_foot)

    l_hand = GPolygon()
    l_hand.add_vertex((133, 190))
    l_hand.add_vertex((153, 190))
    l_hand.add_vertex((165, 230))
    l_hand.add_vertex((145, 230))
    l_hand.filled = True
    l_hand.fill_color = "pink"
    l_hand.color = "pink"
    window.add(l_hand)

    l_paw = GOval(23, 23, x=133, y=175)
    l_paw.filled = True
    l_paw.fill_color = "pink"
    l_paw.color = "pink"
    window.add(l_paw)

    r_hand = GRect(20, 40, x=330, y=190)
    r_hand.filled = True
    r_hand.fill_color = "pink"
    r_hand.color = "pink"
    window.add(r_hand)

    r_paw = GOval(23, 23, x=326, y=175)
    r_paw.filled = True
    r_paw.fill_color = "pink"
    r_paw.color = "pink"
    window.add(r_paw)

    mouth = GOval(10, 25, x=238, y=190)
    window.add(mouth)
    mouth.filled = True
    mouth.fill_color = "coral"


if __name__ == '__main__':
    main()
