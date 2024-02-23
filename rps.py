import random

# Functions to print Win, Lose, or Tie
def win():
    print("You Won!")
def lose():
    print("You Lost! Computer Wins.")  
def tie():
    print("You Tied!")

# Get User's input
print("Rock, Paper, Scissors!")
player = input()
player = player.upper()

# Get Computer input
computer = ""
compchoice = random.randrange(3)
if compchoice == 0:
    computer = "ROCK"
elif compchoice == 1:
    computer = "PAPER"
else:
    computer = "SCISSORS"

# See who wins, loses, or if they tie.
if player == computer:
    tie()
elif player == "ROCK":
    if computer == "PAPER":
        lose()
    elif computer == "SCISSORS":
        win()
elif player == "PAPER":
    if computer == "ROCK":
        win()
    elif computer == "SCISSORS":
        lose()
elif player == "SCISSORS":
    if computer == "ROCK":
        lose()
    elif computer == "PAPER":
        win()
else:
    print("Your input wasn't valid. You lose.")
    
