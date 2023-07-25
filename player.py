from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")            # To give it a turtle shape
        self.penup()                    # To prevent the turtle from drawing
        self.goto(STARTING_POSITION)    # Start position
        self.setheading(90)             # Turtle orientation

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Detect that the turtle has reached the goal and has won
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False