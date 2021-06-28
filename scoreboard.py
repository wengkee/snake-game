from turtle import Turtle
import constants

SCORE_BOARD_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, constants.SCREEN_HEIGHT / 2 - 40)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=SCORE_BOARD_FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_game_over(self):
        # self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=SCORE_BOARD_FONT)

