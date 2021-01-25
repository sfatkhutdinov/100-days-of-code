from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

game_is_on = True
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()

paddle_r = Paddle('right')
screen.onkey(paddle_r.move_up, 'Up')
screen.onkey(paddle_r.move_down, 'Down')

paddle_l = Paddle('left')
screen.onkey(paddle_l.move_up, 'w')
screen.onkey(paddle_l.move_down, 's')

ball = Ball()
while game_is_on:
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 330) \
            or (ball.distance(paddle_l) < 50 and ball.xcor() < -330):
        ball.x_bounce()
        ball.increase_speed()
    if ball.xcor() > 370:
        ball.ball_reset()
        scoreboard.point_left()

    if ball.xcor() < -370:
        ball.ball_reset()
        scoreboard.point_right()

    if scoreboard.r_score == 10 or scoreboard.l_score == 10:
        game_is_on = False

screen.exitonclick()
