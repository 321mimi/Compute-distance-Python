# computeDistance
# By Michelle Cantin
# The formula: Distance = √(x2−x1)2+(y2−y1)2

import math

# The function
def computeDistance(x, y, x1, y1):
    distance = math.sqrt((((x ** 2) - (x ** 1)) ** 2) + (((y ** 2) - (y ** 1)) ** 2))
    distance = round(distance, 2)
    return distance

# Prompts
x = int(input("What is the first coordinate? "))
y = int(input("What is the second coordinate? "))
x1 = int(input("What is the third coordinate? "))
y1 = int(input("What is the fourth coordinate? "))

# Calling the function and prints it
print(computeDistance(x, y, x1, y1))
