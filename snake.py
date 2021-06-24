from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.construct_snake()
        self.head = self.segments[0]

    def construct_snake(self):
        for pos in STARTING_POS:
            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(pos)
            self.segments.append(seg)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            # get pos of the seg in front
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def collided_with_border(self, height, width):
        x = self.head.xcor()
        y = self.head.ycor()
        if x < width / 2 * -1 or x > width / 2:
            return True
        elif y < height / 2 * -1 or y > height / 2:
            return True
        else:
            return False
