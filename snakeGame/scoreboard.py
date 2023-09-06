from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Verdana', 15, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        self.score = 0
        self.high_score = self.highscore()
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def highscore(self):
        file = open("High_Scores.txt", mode="r")
        content = file.read()
        print(content)
        file.close()
        return int(content)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("High_Scores.txt", mode="w") as file:
                file.write(f"{self.score}")
                self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


