import turtle
import csv
from text_manager import TextManager

screen = turtle.Screen()
screen.title("Colombia departments game")
screen.setup(width=980, height=980)
image = "blank_departments_img.gif"

screen.addshape(image)

turtle.shape(image)

text_manager = TextManager()

with open("departments_coordinates.csv", mode="r", encoding="utf-8") as data_file:
    data = list(csv.reader(data_file))

    departments_guessed = 0

    while(departments_guessed < 31):
        answer_department = screen.textinput(title=f"{departments_guessed}/31 Departments guessed", prompt="Write the departments name!")
        if answer_department is None:
            break

        for row_info in data:
            if answer_department.lower() == row_info[0].lower():
                departments_guessed+=1
                text_manager.add_department(row_info[0], int(row_info[1]), int(row_info[2]))
                data.remove(row_info)
        

