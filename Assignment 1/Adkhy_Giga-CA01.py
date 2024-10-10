# Adkhy_Giga-CA01.py October 2024
# Input barge dimensions - Calculate draft of the iron barge - Echo inputs and output surface area, mass and draft

# Input the barge dimensions
length = float(input("Enter the length of the barge in meters: "))
breadth = float(input("Enter the breadth of the barge in meters: "))
height = float(input("Enter the height of the barge in meters: "))

ironWeight = 1.06 # iron weight in kg per meter squared

''' 
Based on the assignment, the formula to calculate the draft of the barge is: mass/(length*breadth)
Mass is obtained by having the surface area of the barge and multiplying it by the weight of iron.
There are 5 sides of the barge - 4 walls and 1 floor. The walls are 2 pieces of length*height and 2 pieces of breadth*height. The floor is length*breadth.
The surface area of the barge is the sum of the surface area of the 5 sides.
'''
# Calculations
surfaceArea = (length*breadth) + 2*(length*height) + 2*(breadth*height)
mass = surfaceArea * ironWeight
draft = mass/(length*breadth)

# Outputs
print("\nThe length of the barge is: ", length, " meter(s).")
print("The breadth of the barge is: ", breadth, " meter(s).")
print("The height of the barge is: ", height, " meter(s).")

print("The surface area of the barge is: ", surfaceArea, " meter(s)^2.")
print("The mass of the barge is: ", mass, " kg(s).")
print("The draft of the barge is: ", draft, " kg(s)/meter^2.")

"""
Test Table
________________________________________________________________________________________________________________________
Test    |   Input Values    |   Expected Output     |   Actual Output       |   Comment
========================================================================================================================
1       |   1, 1, 1         |   5.3                 |   5.300000000000001   |   Error: off by 0.000000000000001
2       |   2, 3, 4         |   8.126666666666667   |   8.126666666666667   |   Pass
3       |   10, 3, 3        |   3.816               |   3.8160000000000003  |   Error: off by 0.0000000000000003
4       |   20, 10, 8       |   3.604               |   3.6040000000000005  |   Error: off by 0.0000000000000005
5       |   5, 15, 10       |   6.713333333333333   |   6.713333333333333   |   Pass
========================================================================================================================
"""