V = 0.0
R =  0.0
E =  0.0
S =  0.0

R = (float(input("Input the length of the row in feet: ")))

E = (float(input("Input the amount of space in feet: ")))

S = (float(input("Input the space between the vines in feet: ")))


V = R - 2 * E / S

print("Amount of Grapevines that will fit the row: ", V)