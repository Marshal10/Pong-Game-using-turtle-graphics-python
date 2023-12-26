from turtle import Turtle

MOVING_DISTANCE=20
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup ()
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.goto(position)
        self.left(90) 
        
    def move(self):
        if self.ycor()==260:
            self.setheading(270)
        elif self.ycor()==-240:
            self.setheading(90)
        self.forward(MOVING_DISTANCE)

        
    def move_down(self):
        if self.ycor()==-240:
            return None
        self.backward(MOVING_DISTANCE)
        
    def move_up(self):
        if self.ycor()>250:
            return None
        self.forward(MOVING_DISTANCE)
        