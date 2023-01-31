
def falling_distance(time):
    return 1/2 * 9.8 * time ** 2

def main():
    time = float(input("Enter the amount of time the object has been falling (in seconds): "))
    print("The object has fallen", falling_distance(time), "meters.")

main()

