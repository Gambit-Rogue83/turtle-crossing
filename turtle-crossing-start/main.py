import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

zippy = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(zippy.cross, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    #Squish
    for car in cars.all_cars:
        if car.distance(zippy) < 20:
            game_is_on = False
            score.game_over()

    #Finish line
    if zippy.finish_line():
        zippy.start_again()
        cars.speed_up()
        score.level_up()

    #Score


screen.exitonclick()