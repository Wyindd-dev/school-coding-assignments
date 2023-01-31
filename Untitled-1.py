import os
import time
if os.name == 'nt':
    os.system( 'cls' )
else:
    os.system( 'clear' )

print("  ______   _______   __     __  ________  __    __  ________  __    __  _______   ________ ")
print("/      \ |       \ |  \   |  \|        \|  \  |  \|        \|  \  |  \|       \ |        \ ")
print("|  $$$$$$\| $$$$$$$\| $$   | $$| $$$$$$$$| $$\ | $$ \$$$$$$$$| $$  | $$| $$$$$$$\| $$$$$$$$")
print("| $$__| $$| $$  | $$| $$   | $$| $$__    | $$$\| $$   | $$   | $$  | $$| $$__| $$| $$__    ")
print("| $$    $$| $$  | $$ \$$\ /  $$| $$  \   | $$$$\ $$   | $$   | $$  | $$| $$    $$| $$  \   ")
print("| $$$$$$$$| $$  | $$  \$$\  $$ | $$$$$   | $$\$$ $$   | $$   | $$  | $$| $$$$$$$\| $$$$$   ")
print("| $$  | $$| $$__/ $$   \$$ $$  | $$_____ | $$ \$$$$   | $$   | $$__/ $$| $$  | $$| $$_____ ")
print("| $$  | $$| $$    $$    \$$$   | $$     \| $$  \$$$   | $$    \$$    $$| $$  | $$| $$     \ ")
print(" \$$   \$$ \$$$$$$$      \$     \$$$$$$$$ \$$   \$$    \$$     \$$$$$$  \$$   \$$ \$$$$$$$$")
print(" ")
input("Press Enter to continue...")

if os.name == 'nt':
    os.system( 'cls' )
else:
    os.system( 'clear' )

time.sleep(2)

if __name__ == "__main__":
  while True:
    print("Welcome to the ship!")
    print("You are first locked in the ship, have to find the way to the city.")
    print("However, trying to escape, you got caught and found back in the ship.")
    print("You can choose to walk in multiple directions and fight your way out.")
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    print("You are in the ship, you can go left.")
    direction = input()
    if direction == "left":
        print("there is a room, would you like to enter it?")
        answer = input()
        if answer == "yes":
            print("You are in a dark room, you can see a light in the distance.")
            print("Would you like to go towards the light?")
            answer = input()
            if answer == "yes":
                print("You are now on the ship's deck, you can see the city.")
                print("You can go towards the city.")
                direction = input()
                if direction == "city":
                    print("You are now in the city, you can see a castle.")
            elif answer == "no":
                print("You are stuck. You can't go anywhere.")
                print("You are dead.")
                break
            else:
                print("You can't do that.")
                print("You are dead.")
                break
            if answer == "yes":
                print("You are now in the castle, you can see a door.")
                print("Would you like to go through the door?")
                answer = input()
                if answer == "yes":
                    print("You are now in the castle's throne room.")
                    print("You can see a king.")
                    print("Would you like to talk to the king?")
                    answer = input()
                    if answer == "yes":
                        print("You are now talking to the king.")
                        print("The king asks you to kill the dragon.")
                        print("Would you like to do that?")
                        answer = input()
                        if answer == "yes":
                            print("You are now fighting the dragon.")
                            print("You killed the dragon.")
                            print("You are now the king.")
                            print("You win.")
                            break
                        elif answer == "no":
                            print("You are now dead.")
                            break
                        else:
                            print("You can't do that.")
                            print("You are dead.")
                            break
                    elif answer == "no":
                        print("You are now dead.")
                        break
                    else:
                        print("You can't do that.")
                        print("You are dead.")
                        break
                elif answer == "no":
                    print("You are now dead.")
                    break
                else:
                    print("You can't do that.")
                    print("You are dead.")
                    break
