#write a program that asks the user to enter the replacement cost of a building, then displays the minimum amount of insurance he or she should by for the property.

def main():
    replacement_cost = float(input("Enter the replacement cost of the building: "))
    min_insurance = replacement_cost * 0.8
    print("The minimum amount of insurance you should buy is: $", min_insurance)

main()