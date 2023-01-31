#get the number of years
years = int(input('For how many years do you have data? '))
#set accumulator
total_months = 0
total_inches = 0
#calculate the average rainfall for each year
for year in range(years):
    print('Year ', year + 1)
    for month in range(1, 13):
        inches = float(input('Enter the inches of rainfall for month ' + str(month) + ': '))
        total_months += 1
        total_inches += inches
#display the results
print('Total months: ', total_months)
print('Total inches of rainfall: ', total_inches)
print('Average rainfall per month: ', format(total_inches / total_months, '.2f'))