# Adkhy_Giga-CA01.py October 2024
# Input barge dimensions - Calculate draft of an iron barge - Echo inputs and output surface area, mass and draft

# Input the barge dimensions
length = float(input("Enter the length of the barge in meters: "))
breadth = float(input("Enter the breadth of the barge in meters: "))
height = float(input("Enter the height of the barge in meters: "))

ironWeight = 1.06 # iron weight in kg per meter squared

''' 
Based on the assignment, the formula to calculate the draft of the barge is: mass/(length*breadth)
Calculate the mass of the barge. Mass is obtained by having the surface area of the barge and multiplying it by the weight of iron.
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
Test    |   Input Values    |   Expected Output |   Actual Output   |   Pass/Fail
1       |   2, 3, 4         |   1.06            |   1.06            |   Pass
2       |   3, 4, 5         |   1.06            |   1.06            |   Pass
3       |   4, 5, 6         |   1.06            |   1.06            |   Pass
4       |   5, 6, 7         |   1.06            |   1.06            |   Pass
5       |   6, 7, 8         |   1.06            |   1.06            |   Pass
"""