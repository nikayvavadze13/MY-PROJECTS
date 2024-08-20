import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = input("enter rock/paper/scissors: ").lower()

if player not in choices:
    print("thats not a choice!")

if player == computer:
    print("computer: ", computer)
    print("player: ", player)
    print("Tie!")
elif player == "rock":
    if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("you lost! :(")
    else:
        print("computer: ", computer)
        print("player: ", player)
        print("CONGRATULATION!!! YOU WON! :)")
elif player == "paper":
    if computer == "scissors":
        print("computer: ", computer)
        print("player: ", player)
        print("you lost! :(")
    else:
        print("computer: ", computer)
        print("player: ", player)
        print("CONGRATULATION!!! YOU WON! :)")
elif player == "scissors":
    if computer == "rock":
        print("computer: ", computer)
        print("player: ", player)
        print("you lost! :(")
    else:
        print("computer: ", computer)
        print("player: ", player)
        print("CONGRATULATION!!! YOU WON! :)")

