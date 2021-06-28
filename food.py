import random
from turtle import Turtle
import constants

BUFFER_X_FROM_BORDER = (constants.SCREEN_WIDTH / 2) - 20
BUFFER_Y_FROM_BORDER = (constants.SCREEN_HEIGHT / 2) - 20


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        # self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("yellow")
        self.speed("fastest")
        self.generate()

    def generate(self):
        random_x = random.randint(BUFFER_X_FROM_BORDER * -1, BUFFER_X_FROM_BORDER)
        random_y = random.randint(BUFFER_Y_FROM_BORDER * -1, BUFFER_Y_FROM_BORDER)
        self.goto(random_x, random_y)
