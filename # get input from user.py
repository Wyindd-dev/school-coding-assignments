# get input from user

from turtle import goto


day = 0

day = int(input('enter a number (1-7) for the day of the week: '))

# Determine the name of the day of the week, and prints to the screen.

if day == 1:
    print ("Monday")
elif day == 2:
    print ("Tuesday")
elif day == 3:
    print ("Wednesday")
elif day == 4:
    print ("Thursday")
elif day == 5:
    print ("Friday")
elif day == 6:
    print ("Saturday")
elif day == 7:
    print ("Sunday")

else:
    print("Error, invalid value! please try again.")