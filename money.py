pennies = int(input("Enter the number of pennies: "))
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quart = int(input("Enter the number of quarters: "))

total = pennies + nickels + dimes + quart

if total == 100:
    print("Congratulations, you won the game!")
elif total > 100:
    print("The amount you entered is more than one dollar.")
else:
    print("The amount you entered is less than one dollar.")

    