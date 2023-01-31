#prompt the user to enter the names of two primary colors to mix
primary_color1 = input("Enter the name of a primary color to mix in lowercase: ")
primary_color2 = input("Enter the name of a primary color to mix in lowercase: ")

#determine the secondary color
if primary_color1 == "red" and primary_color2 == "blue":
    print("When you mix red and blue, you get purple!")
elif primary_color1 == "blue" and primary_color2 == "red":
    print("When you mix red and blue, you get purple!")
elif primary_color1 == "red" and primary_color2 == "yellow":
    print("When you mix red and yellow, you get orange!")
elif primary_color1 == "yellow" and primary_color2 == "red":
    print("When you mix red and yellow, you get orange!")
elif primary_color1 == "blue" and primary_color2 == "yellow":
    print("When you mix blue and yellow, you get green!")
elif primary_color1 == "yellow" and primary_color2 == "blue":
    print("When you mix blue and yellow, you get green!")
else:
    print("Error: Invalid color name!")
