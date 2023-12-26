from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_cor=0
        self.y_cor=0
        self.goto((self.x_cor,self.y_cor))
        
    def move(self):
        self.x_cor+=-10
        self.y_cor+=-10
        #if self.xcor()==350:
            
        self.goto((self.x_cor,self.y_cor))