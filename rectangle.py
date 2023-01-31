# Ask user to enter length and width of rectangle 1
length1 = int(input("Enter length of rectangle 1: "))
width1 = int(input("Enter width of rectangle 1: "))
# Ask user to enter length and width of rectangle 2
length2 = int(input("Enter length of rectangle 2: "))
width2 = int(input("Enter width of rectangle 2: "))
# Calculate area of rectangle 1
area1 = length1 * width1
# Calculate area of rectangle 2
area2 = length2 * width2
# Compare areas of rectangles
if area1 > area2:
    print("Rectangle 1 has the greater area.")
elif area2 > area1:
    print("Rectangle 2 has the greater area.")
else:
    print("The areas are the same.")