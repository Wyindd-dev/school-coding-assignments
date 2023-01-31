
def main():
    loan_payment = float(input("Enter the monthly loan payment: "))
    insurance = float(input("Enter the monthly insurance cost: "))
    gas = float(input("Enter the monthly gas cost: "))
    oil = float(input("Enter the monthly oil cost: "))
    tires = float(input("Enter the monthly tires cost: "))
    maintenance = float(input("Enter the monthly maintenance cost: "))
    monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance
    annual_cost = monthly_cost * 12
    print("The total monthly cost is: ", monthly_cost)
    print("The total annual cost is: ", annual_cost)

main()