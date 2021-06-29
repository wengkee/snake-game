from turtle import Turtle
import constants
import os

SCORE_BOARD_FONT = ("Courier", 24, "normal")
DATA_FILE = "high_score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        if os.path.exists(DATA_FILE):
            print("EXISTS")
            file_mode = "r"
        else:
            file_mode = "w+"

        print(file_mode)

        with open(DATA_FILE, mode=file_mode) as f:
            content = f.read()
            print(content)
            if content:
                self.high_score = int(content)
            else:
                self.high_score = 0

            print(self.high_score)

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, constants.SCREEN_HEIGHT / 2 - 40)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore:{self.high_score}", align="center", font=SCORE_BOARD_FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_FILE, mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_game_over(self):
        # self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=SCORE_BOARD_FONT)

