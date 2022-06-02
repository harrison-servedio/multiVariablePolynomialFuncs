# Function that takes "rock", "paper", or "scissors" as input generates a random choice and compares the two
#
def rps():
    import random
    choices = ["rock", "paper", "scissors"]
    player = input("rock, paper, or scissors? ")
    computer = random.choice(choices)
    print("You chose", player, "and the computer chose", computer)
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    print("Do you want to play again? (y/n)")
    answer = input()
    if answer == "y":
        rps()
    else:
        print("Thanks for playing!")
rps()