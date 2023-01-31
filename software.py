# Get the number of packages purchased.
num_packages = int(input("Enter the number of packages purchased: "))
# Determine the amount of the discount.
if num_packages < 10:
    discount = 0
elif num_packages < 20:
    discount = 10
elif num_packages < 50:
    discount = 20
elif num_packages < 100:
    discount = 30
else:
    discount = 40
# Calculate the total amount of the purchase after the discount.
total = num_packages * 99
discount_amount = total * discount / 100
total -= discount_amount
# Display the amount of the discount and the total amount of the purchase after the discount.
print("Amount of discount: $", format(discount_amount, ",.2f"), sep="")
print("Total amount: $", format(total, ",.2f"), sep="")
