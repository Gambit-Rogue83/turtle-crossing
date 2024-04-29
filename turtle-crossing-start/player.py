from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_again()
        self.seth(90)

    def cross(self):
        self.fd(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def start_again(self):
        self.goto(STARTING_POSITION)