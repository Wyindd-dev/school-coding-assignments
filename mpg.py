import os
import time
shares = 2000.00
purchase = 40.00
percent = 0.03
sell = 42.75

broker = purchase * percent

if os.name == "nt":
     os.system('cls')
if os.name == "posix":
    os.system('clear')

print ("Joe bought the stock (in dollars) for:  ", purchase)
time.sleep(2)
print ("Joe's Commission to the broker (in dollars) is: ", broker)
time.sleep(2)
print("Joe sold the stock for: ", sell)