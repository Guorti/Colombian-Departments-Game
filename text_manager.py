from turtle import Turtle
FONT = ("Courier", 10, "bold")
class TextManager():
    def __init__(self):
        self.text_instances = []

    def add_department(self, department_name: str, x_pos: int, y_pos: int):
        text = Turtle()
        text.penup()
        text.hideturtle()
        text.color("black")
        text.goto(x_pos, y_pos)
        text.write(department_name, align="center", font=FONT)
    

