
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
    for i in range(1, 101):
        if is_prime(i):
            print(i)

main()
