from turtle import Turtle
STARTING_POSITION=[(-420,0),(-420,-20),(-420,-40)]

MOVING_DISTANCE=20
class Paddle():

    def __init__(self):
        super().__init__()
        self.segments=[]
        self.create_paddle()
        self.head=self.segments[0]
    
    def create_paddle(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
        
    def add_segment(self,position):
        segment=Turtle(shape='square')
        segment.color('white')
        segment.penup ()
        segment.goto(position)
        segment.left(90)
        self.segments.append(segment)
        
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVING_DISTANCE)
        
    def move_down(self):
        if self.head.heading()==90:
            self.segments=self.segments[::-1]
            self.head=self.segments[0]
            self.head.setheading(270)
        self.move()
        
    def move_up(self):
        if self.head.heading()==270:
            self.segments=self.segments[::-1]
            self.head=self.segments[0]
            self.head.setheading(90)
        self.move()
        