
# Define the variables
total_sales = 0.0
county_tax = 0.0
state_tax = 0.0
total_tax = 0.0

# Get the total sales
total_sales = float(input("Enter the total sales for the month: "))
# Calculate the county tax
county_tax = total_sales * 0.025
# Calculate the state tax
state_tax = total_sales * 0.05
# Calculate the total tax
total_tax = county_tax + state_tax
# Display the results
print("The amount of county sales tax is $", format(county_tax, ",.2f"), sep="")
print("The amount of state sales tax is $", format(state_tax, ",.2f"), sep="")
print("The total sales tax is $", format(total_tax, ",.2f"), sep="")
