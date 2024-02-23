import random

options = ["rock", "scissors", "paper"]


draw = "result is draw"
win = "result is win"
lose = "result is lose"


def main():

    for _ in range(2):
        p1choice = input("rock paper or scissors?")
        computer_choice = random.choice(options)
        print(computer_choice)

    match (p1choice, computer_choice):
        case (p, c) if p == c:
            print(draw)
        case ("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
            print(win)
        case _:
            print(lose)


main()
