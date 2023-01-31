#prompt the user to enter the number of people attending the cookout and the number of hotdogs each person will be given
people = int(input("Enter the number of people attending the cookout: "))
hotdogs = int(input("Enter the number of hotdogs each person will be given: "))
#calculate the number of hotdogs needed
hotdogs_needed = people * hotdogs
#calculate the number of hotdog buns needed
buns_needed = people * hotdogs
#calculate the number of packages of hotdogs required
hotdogs_packages = hotdogs_needed // 10
#calculate the number of packages of hotdog buns required
buns_packages = buns_needed // 8
#calculate the number of hotdogs that will be left over
hotdogs_leftover = hotdogs_needed % 10
#calculate the number of hotdog buns that will be left over
buns_leftover = buns_needed % 8
#display the results
print("The minimum number of packages of hotdogs required is", hotdogs_packages)
print("The minimum number of packages of hotdog buns required is", buns_packages)
print("The number of hotdogs that will be left over is", hotdogs_leftover)
print("The number of hotdog buns that will be left over is", buns_leftover)
