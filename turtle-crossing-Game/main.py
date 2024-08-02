import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

new_player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=new_player.go_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(new_player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if new_player.is_at_finish_line():
        new_player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
