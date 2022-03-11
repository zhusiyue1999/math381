import math

# This code is used to generate a lp input file for a knapsack problem.

#Gives the objective function.
output = "max: "
for i in range(1,101):
    val = math.floor(50 + 25*math.cos(5*i))
    output = output + "+" + str(val) + "x" + str(i)
output = output + ";"
print(output)

#Gives the weight constraint, which is the total weight is <= 300.
output = "weight = "
for i in range(1,101):
    weight = math.floor(30 + 12 * math.cos(4*i+1))
    output = output + "+" + str(weight) + "x" + str(i)
output = output + ";"
print(output)
print("weight <= 300;")

#Gives the volume constraint, which is the total volume is <= 300.
output = "volume = "
for i in range(1,101):
    volume = math.floor(30 + 12 * math.cos(2*i+2))
    output = output + "+" + str(volume) + "x" + str(i)
output = output + ";"
print(output)
print("volume <= 300;")

# Count the number of our objects picked.
output = "count = "
for i in range(1,100):
    output = output + "x" + str(i) + "+"
output = output + "x100;"
print(output)
print("count >= 1;")

# Set the variable constraint.
output = "int "
for i in range(1,100):
    output = output + "x" + str(i) + ","
output = output + "x100;"
print(output)
