import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
chutiya_player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(chutiya_player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collison with the cars
    for car in car_manager.all_cars:
        if car.distance(chutiya_player) < 30:

            game_is_on = False
            scoreboard.game_over()

    # detect finishing line
    if chutiya_player.is_at_finishline():
        chutiya_player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()
