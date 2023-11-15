from robot import Robot, Robot2, Robot3
from campy.graphics.gwindow import GWindow

print("robot_starter.py" + __name__)

def main():
    r1 = Robot(160, 50)
    ball1 = r1.give_me_a_ball(500)
    window = GWindow()
    window.add(ball1)
    r1.self_intro()
    r1.bmi()
    r1.say_hi()
    Robot.say_hi()

    r2 = Robot2(180, 65, color2="tomato", count2=5)

    r3 = Robot3(185, 70, "sky blue")
    rect = r3.give_me_a_rect(400)
    window.add(rect)


if __name__ == '__main__':
    main()
