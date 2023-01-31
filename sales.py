tips = 0.0
tax = 0.07
total = 0.0
def main():
    purchase = float(input("input the price of the food: "))
    tips = float(input("input the price of the tip: "))
    total = tips + tax + purchase
    print("Your total is: ", format(total, '.2f'))

main()

#