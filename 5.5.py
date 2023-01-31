#write a program that gives simple math quizzes. The program should display two random numbers that are to be added, such as:
# 247
#+ 129
#-----
#The program should allow the student to enter the answer. If the answer is correct, a message of congratulations should be printed. If the answer is incorrect, a message should be printed showing the correct answer.

import random
num1 = random.randint(0, 1000)
num2 = random.randint(0, 1000)
print(num1)
print("+", num2)
print("-----")
answer = int(input("Enter your answer: "))
if answer == num1 + num2:
    print("Congratulations! You got it right!")
else:
    print("Sorry, the correct answer is", num1 + num2)
