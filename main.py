from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time


screen=Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.setup(width=800,height=600)

paddle1=Paddle((-360,0))
paddle2=Paddle((350,0))
ball=Ball()

screen.onkey(paddle1.move_up,"w")
screen.onkey(paddle1.move_down,"s")

screen.onkey(paddle2.move_up,"Up")
screen.onkey(paddle2.move_down,"Down")
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    
    
    ball.move()
    
    
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce()
    
    
    if ball.distance(paddle1)<50 and ball.xcor()<-320 or ball.distance(paddle2)<50 and ball.xcor()>320:
        ball.bounce_of_paddle()

    
    






screen.exitonclick()