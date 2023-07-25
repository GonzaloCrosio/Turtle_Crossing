from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.level = 1
            self.hideturtle()          # To hide the turtle
            self.penup()               # To prevent the turtle from drawing
            self.goto(-280, 260)       # Score location
            self.update_scoreboard()

        def update_scoreboard(self):
            self.clear()
            self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the level

        def increase_level(self):
            self.level += 1
            self.update_scoreboard()

        def game_over(self):
            self.goto(0, 0)
            self.write("GAME OVER", align="center", font=FONT)  # Write the level
