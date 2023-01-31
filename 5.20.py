import random

def main():
    number = random.randint(1, 100)
    guess = int(input("Guess a number: "))
    count = 1
    while guess != number:
        if guess > number:
            print("Too high, try again.")
        else:
            print("Too low, try again.")
        guess = int(input("Guess a number: "))
        count += 1
    print("Congratulations! You guessed the number!")
    print("It only took you", count, "tries!")

main()

