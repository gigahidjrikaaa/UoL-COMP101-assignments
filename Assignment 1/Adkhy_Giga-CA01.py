# Adkhy_Giga-CA01.py October 2024
# Input barge dimensions - Calculate draft of an iron barge - Echo inputs and output surface area, mass and draft

# Input the barge dimensions
length = float(input("Enter the length of the barge in meters: "))
breadth = float(input("Enter the breadth of the barge in meters: "))
height = float(input("Enter the height of the barge in meters: "))

ironWeight = 1.06 # iron weight in kg per meter squared

''' 
Based on the assignment, the formula to calculate the draft of the barge is: mass/(length*breadth)
Mass is obtained by having the surface area of the barge and multiplying it by the weight of iron.
There are 5 sides of the barge - 4 walls and 1 floor.
The surface area of the barge is the sum of the surface area of the 5 sides.
'''
surfaceArea = (length*breadth) + 2*(length*height) + 2*(breadth*height)
mass = surfaceArea * ironWeight
draft = mass/(length*breadth)

# Outputs
print("The length of the barge is: ", length)
print("The breadth of the barge is: ", breadth)
print("The height of the barge is: ", height)

print("The surface area of the barge is: ", surfaceArea)
print("The mass of the barge is: ", mass)
print("The draft of the barge is: ", draft)

"""
Test Table
Test    |   Input Values    |   Expected Output     |   Actual Output       |   Comment
1       |   1, 1, 1         |   5.3                 |   5.300000000000001   |   Error: off by 0.000000000000001
2       |   2, 3, 4         |   8.126666666666667   |   8.126666666666667   |   Pass
3       |   10, 3, 3        |   3.816               |   3.8160000000000003  |   Error: off by 0.0000000000000003
4       |   20, 10, 8       |   3.604               |   3.6040000000000005  |   Error: off by 0.0000000000000005
5       |   5, 15, 10       |   6.713333333333333   |   6.713333333333333   |   Pass
"""