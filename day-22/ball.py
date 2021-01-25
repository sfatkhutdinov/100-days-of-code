from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.speed(1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.counter = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def ball_reset(self):
        self.speed(0)
        self.hideturtle()
        self.goto(0, 0)
        self.speed(1)
        self.showturtle()
        self.x_bounce()
        self.speed(1)
        self.counter = 1

    def increase_speed(self):
        self.speed(self.counter)
        self.counter += 0.10
