from turtle import Screen,Turtle
from paddle import Paddle
import time

STARTING_COMPUTER_POSITION=[(410,0),(410,-20),(410,-40)]

screen=Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.setup(900,700)

paddle1=Paddle()
paddle2=Paddle()

for i in range(3):
    paddle2.segments[i].goto(STARTING_COMPUTER_POSITION[i])
#screen.onkey(paddle1.move_up,"w")
#screen.onkey(paddle1.move_down,"s")
screen.onkey(paddle1.move_up,"Up")
screen.onkey(paddle1.move_down,"Down")

while True:
    screen.update()
    time.sleep(0.1)
    if paddle2.head.ycor()==340:
        paddle2.move_down()
    elif paddle2.head.ycor()==-340:    
        paddle2.move_up()
    else:
        paddle2.move()
    

    
    






screen.exitonclick()