# one foot = to 12 inches 
#write a function named feet_to_inches that accepts a number of feet as an argment and returns the number of inches in that many feet. use the function  in a program that prompts the user to enter a number of feet and then displays the number of inches in that many feet.

def feet_to_inches(feet):
    return feet * 12

def main():
    feet = int(input("Enter the number of feet: "))
    print(feet, "feet equals", feet_to_inches(feet), "inches")

main()
