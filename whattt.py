# write a program that sks the user to enter the amou t that he or she has budgeted for a month
# a loop should then prompt the user to enter each of his or her expenses for the month and keep a running total
# when the loop finishes, the program should display the amount that the user is over or under budget

# get the budget
budget = float(input("Enter the budget for the month: "))
# initialize an accumulator for the expenses
expenses = 0.0
# get the first expense
expense = float(input("Enter an expense or -1 to quit: "))
# loop until the user enters -1
while expense != -1:
    # add the expense to the accumulator
    expenses += expense
    # get the next expense
    expense = float(input("Enter an expense or -1 to quit: "))
# display the amount over or under budget
if expenses > budget:
    print("You were over budget by $", format(expenses - budget, ",.2f"), sep="")
else:
    print("You were under budget by $", format(budget - expenses, ",.2f"), sep="")
