#asks speed
speed = int(input("What is the speed of the vehicle in mph? "))
#asks time
time = int(input("How many hours has it traveled? "))
#displays speed and time
print("Hour Distance Traveled")
for i in range(1, time + 1):
    print(i, speed * i)