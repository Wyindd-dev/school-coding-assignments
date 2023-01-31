#create a table of celsius and fahrenheit equivalents
print('Celsius\tFahrenheit')
for celsius in range(21):
    fahrenheit = 9/5 * celsius + 32
    print(celsius, '\t', format(fahrenheit, '.1f'))

#ask the user for a temprature in celcius
celsius = float(input('Enter a temperature in celsius: '))
#convert the temperature to fahrenheit
fahrenheit = 9/5 * celsius + 32
#display the temperature in fahrenheit
print('The temperature is', format(fahrenheit, '.1f'), 'degrees fahrenheit.')
