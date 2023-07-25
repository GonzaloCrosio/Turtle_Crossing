import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()                     # Player creator
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()                       # Listen to events
screen.onkey(player.go_up, "Up")      # Event key up - command Up

game_is_on = True
while game_is_on:
    time.sleep(0.1)                  # The screen refreshes every 0.1 seconds
    screen.update()
    car_manager.create_car()         # To have a car created with every screen refresh
    car_manager.move_cars()

    # Detect the collision of the turtle with the car. If the distance is less than 20 between the turtle and the car, it's Game over.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect that the turtle successfully crosses the paddle
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()