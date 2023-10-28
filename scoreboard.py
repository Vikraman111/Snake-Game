from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,210)
        self.write(arg=f"SCORE: {self.score}", move=False, align="center", font=("Arial", 21, "normal"))
        self.hideturtle()

    def increase_Score(self):
        self.score += 1
        self.clear()
        self.goto(0,210)
        self.write(arg=f"SCORE: {self.score}", move=False, align="center", font=("Arial", 21, "normal"))
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nYour score is {self.score} ",align="center",font = ("",25,"normal"))
