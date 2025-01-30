import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
cars = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.go_up, 'Up')

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()


    cars.create_car()
    cars.move_cars()

    for car in cars.cars_list:
        if car.distance(player) < 20:
            is_game_on = False
            score.game_over()
    if player.is_at_finish_line():
        player.start_position()
        score.increase_score()
        cars.level_up()

screen.exitonclick()