import time
import constants

from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT)
screen.title("Snake Game")
screen.tracer(0)

s = Snake()
f = Food()
sb = Scoreboard()

screen.listen()
screen.onkey(s.up, "w")
screen.onkey(s.down, "s")
screen.onkey(s.left, "a")
screen.onkey(s.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

    # Collision with food
    if s.head.distance(f) < 15:
        sb.update_score()
        s.grow()
        f.generate()

    # Collision with border / body
    # game_is_on = not s.collided_with_border() and not s.collided_with_body()
    if s.collided_with_border() or s.collided_with_body():
        sb.reset()
        s.reset()

# sb.update_game_over()
screen.exitonclick()
