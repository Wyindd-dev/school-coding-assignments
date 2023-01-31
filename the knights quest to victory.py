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


print("What is your name?")
name = input()
print("Hello, " +name+ ".")

print("You are a knight.")

print("You are in a castle.")
print("You can go left or right.")
direction = input()
if direction == "left":
        print("You are in the throne room.")
        print("You can see the king.")
        print("Would you like to talk to the king?")
        answer = input()
        if answer == "yes":
            print("You are now talking to the king.")
            print("The king asks you to kill the dragon. If you do, you will be rewarded by becoming the king.")
            print("Would you like to do that?")
            answer = input()
            if answer == "yes":
                print("You can choose between 2 weapons. A sword or a bow.")
                weapon = input()
                if weapon == "sword":
                    print("You have chosen the sword.")
                if weapon == "bow":
                    print("You have chosen the bow.")
                    print("You are now fighting the dragon.")
                print("You killed the dragon.")
                print("You are now the king.")
                print("You win.")
            elif answer == "no":
                print("The king is angry.")
                print("A dragon appears.")
                print("the guard kills you. and then you burn to a crisp.")
                print("You died.")
            else:
                print("You can't do that.")
                print("You are dead.")
elif direction == "right": 
    print("You are now dead.")
    print("you fell in to a pit and lost.")
            
else:
    print("You can't do that.")
    print("You are dead.")
                
               