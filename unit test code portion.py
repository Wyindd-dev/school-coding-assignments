#imports time, delete if its not able to run in the online complier, just wanting it to be a little bit neater. :)

import time

#prompt for the number of students in the class
num_students = int(input("How many students are in the class? "))

#prompt for the number of tests per student
num_tests = int(input("How many tests are in the whole class? "))

#initialize the total of the class
total_class = 0

#loop through the students
for student in range(num_students):
    #initialize the total of the student
    total_student = 0
    
    #loop through the tests
    for test in range(num_tests):
        #prompt for the test score
        score = int(input("Enter the test score: "))
        #add the score to the total of the student
        total_student += score
    #calculate the average of the student
    average_student = total_student / num_tests
    #add the average of the student to the total of the class
    total_class += average_student
    #output the average of the student
    print("The average of the student is", average_student)
    break
time.sleep(2)
#calculate the average of the class
average_class = total_class / num_students
#output the average of the class
print("The average of the class is", average_class)
time.sleep(2)
#output the results in a table format
print("Student\t\tAverage")
for student in range(num_students):
    print(student + 1, "\t\t", average_student)


