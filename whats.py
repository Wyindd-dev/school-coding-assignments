import time

# gallons of gas
gallon_of_gas = 0.0
miles_driven = 0.0
miles = 0.0

purchase2 = float(input("Enter the miles driven: "))

# get user input on how much gas was used

gallon_of_gas = float(input("enter the amount of gas used in gallons: "))

#calculate the MPG

mpg = miles_driven / gallon_of_gas

# print result

print("you used:", format(mpg, '.2f'))