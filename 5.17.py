
def is_prime(number):
    if number == 2:
        return True
    elif number < 2 or number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True

def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print("The number is prime.")
    else:
        print("The number is not prime.")

main()

