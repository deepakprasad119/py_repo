# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

# For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.

# Function Description

# Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

# countingValleys has the following parameter(s):

# n: the number of steps Gary takes
# s: a string describing his path

# Sample Input
# 8
# UDDDUDUU

# Sample Output
# 1


import math
import os
import random
import re
import sys

# Complete the countingValleys function below.

sea_level = 0
U = 1
D = -1

n = 8
s = "UDDDUDUU"


list1 = list(s)
list2 = []

for i in range(len(list1)):

    if list1[i] == "U":
        list2.append("1")
    elif list1[i] == "D":
        list2.append("-1")
    else:
        pass

print(list2)

x = 0
counter = 0
for i in range(len(list2)):
    x = x + int(list2[i])
    j = i + 1
    # print(list2[j])
    if x == 0 and x + int(list2[j]) < 0:
        counter = counter + 1

print(counter)




def countingValleys(n, s):
    pass


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     s = input()

#     result = countingValleys(n, s)

#     fptr.write(str(result) + '\n')

#     fptr.close()
