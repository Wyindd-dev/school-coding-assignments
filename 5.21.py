import random

def main():
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    elif computer == 3:
        computer = "scissors"
    user = input("Enter your choice: ")
    print("The computer chose", computer)
    if user == "rock" and computer == "scissors":
        print("You win!")
    elif user == "scissors" and computer == "paper":
        print("You win!")
    elif user == "paper" and computer == "rock":
        print("You win!")
    elif user == computer:
        print("You tied!")
    else:
        print("You lose!")

main()

