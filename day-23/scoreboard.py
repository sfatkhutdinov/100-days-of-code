from turtle import Turtle

FONT = ('Courier', 24, 'normal')
ALIGNMENT = 'left'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.current_level += 1
        self.write(f'Level: {self.current_level}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
