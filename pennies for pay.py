
#ask the user for the number of days
days = int(input('Enter the number of days: '))
#set accumulator
total_pay = 0
#display the table
print('Day\tSalary')
print('----------------')
#calculate the salary for each day
for day in range(1, days + 1):
    salary = 2 ** (day - 1) / 100
    total_pay += salary
    print(day, '\t$', format(salary, '.2f'), sep='')
#display the total pay
print('The total pay is $', format(total_pay, '.2f'), sep='')
