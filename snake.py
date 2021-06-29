from turtle import Turtle

import constants

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

BORDER_COLLISION_X = (constants.SCREEN_WIDTH / 2) -10
BORDER_COLLISION_Y = (constants.SCREEN_HEIGHT / 2)


class Snake:

    def __init__(self):
        self.segments = []
        self.construct_snake()
        self.head = self.segments[0]

    def construct_snake(self):
        for pos in STARTING_POS:
            self.add_new_segment(pos)

    def add_new_segment(self, position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)

    def grow(self):
        last = self.segments[-1]
        self.add_new_segment(last.position())

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

    def collided_with_border(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if x < BORDER_COLLISION_X * -1 or x > BORDER_COLLISION_X \
                or y < BORDER_COLLISION_Y * -1 or y > BORDER_COLLISION_Y:
            return True
        else:
            return False

    def collided_with_body(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return True
        return False

    def reset(self):
        for seg in self.segments:
            seg.goto(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

        self.segments.clear()
        self.construct_snake()
        self.head = self.segments[0]
