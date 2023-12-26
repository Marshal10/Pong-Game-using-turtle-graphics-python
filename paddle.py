from turtle import Turtle

MOVING_DISTANCE=20
class Paddle():

    def __init__(self):
        self.paddle=[]
        self.create_paddle()
        self.head=self.paddle[0]
    
    def create_paddle(self):
        segment=Turtle(shape='square')
        segment.color('white')
        segment.penup ()
        segment.shapesize(stretch_len=5,stretch_wid=1)
        segment.goto((-380,0))
        segment.left(90) 
        self.paddle.append(segment)
        
        
        
    def move(self):
        if self.head.ycor()==260:
            self.head.setheading(270)
        elif self.head.ycor()==-240:
            self.head.setheading(90)
        self.head.forward(MOVING_DISTANCE)

        
    def move_down(self):
        if self.head.ycor()==-240:
            return None
        self.head.backward(MOVING_DISTANCE)
        
    def move_up(self):
        if self.head.ycor()>250:
            return None
        self.head.forward(MOVING_DISTANCE)
        