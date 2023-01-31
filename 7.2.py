import random

def main():
    lotto = []
    for i in range(7):
        lotto.append(random.randint(0,9))
    print(lotto)

 #write another loop that displays the contents of the list.

    for i in lotto:
        print(i, end='')
    print()


main()