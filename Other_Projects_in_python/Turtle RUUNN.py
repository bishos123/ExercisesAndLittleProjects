from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Loop para garantir que o usuário escolha uma cor válida
user_bet = None
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet not in colors:
        print(f"Erro: {user_bet} não é uma cor válida. Por favor, escolha uma das seguintes: {', '.join(colors)}.")

# Criar 6 tartarugas
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 é 250 - metade da largura da tartaruga
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Fazer cada tartaruga mover uma quantidade aleatória
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()