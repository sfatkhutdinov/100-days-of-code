from turtle import Turtle
LEFT = (-350, 0)
RIGHT = (350, 0)

class Paddle(Turtle):

    def __init__(self, position='right'):
        super().__init__()
        self.speed(0)
        if position == 'left':
            self.setpos(LEFT)
        else:
            self.setpos(RIGHT)
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




