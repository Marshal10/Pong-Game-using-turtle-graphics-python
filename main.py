from turtle import Screen,Turtle
from paddle import Paddle
import time


screen=Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
screen.setup(800,600)

paddle1=Paddle()
paddle2=Paddle()

paddle2.head.goto((370,0))
#screen.onkey(paddle1.move_up,"w")
#screen.onkey(paddle1.move_down,"s")

screen.onkey(paddle1.move_up,"Up")
screen.onkey(paddle1.move_down,"Down")
while True:
    screen.update()
    time.sleep(0.1)
    
      

    
    
    paddle2.move()
    
    

    
    






screen.exitonclick()