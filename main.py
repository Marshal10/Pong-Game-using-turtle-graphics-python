from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
player1_score=Scoreboard((-100,200))
player2_score=Scoreboard((100,200))

screen.onkeypress(paddle1.move_up,"w")
screen.onkeypress(paddle1.move_down,"s")

screen.onkeypress(paddle2.move_up,"Up")
screen.onkeypress(paddle2.move_down,"Down")

game_on=True
while game_on:
    screen.update()
    time.sleep(ball.speed)
    
    ball.move()
    
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce()
    
    
    if ball.distance(paddle1)<50 and (ball.xcor() <= -340 and ball.xcor() >= -350):
        ball.bounce_of_paddle()
        ball.increase_speed()
        
    if ball.distance(paddle2)<50 and (ball.xcor()>=340 and ball.xcor()<=350) :     
        ball.bounce_of_paddle()
        ball.increase_speed()
        
    if ball.xcor()>380:
        player1_score.increase_score()
        player1_score.display_score()
        ball.refresh()
        
    elif ball.xcor()<-380:
        player2_score.increase_score()
        player2_score.display_score()
        ball.refresh()
        

screen.exitonclick()