from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.display_score()
        self.hideturtle()
        
    def display_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Courier", 80, "normal"))

    def increase_score(self):
        self.score += 1
