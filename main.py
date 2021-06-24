import time

from snake import Snake
from turtle import Screen

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Snake Game")
screen.tracer(0)

s = Snake()
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
    game_is_on = not s.collided_with_border(width=WIDTH, height=HEIGHT)

print(f"Game Over! Score is {len(s.segments)-3}")
screen.exitonclick()
