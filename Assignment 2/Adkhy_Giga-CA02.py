# Adkhy_Giga 201847335  October2024 CA-02.py
# Finding out if a rover can return to its starting point after travelling a certain time and angle, also provide rover status.

import math

speed = 1.5         # Speed in m/s
battery = 100       # Battery in percentage
battery_usage = 2.7 # Battery usage in percentage per second
status = ["RETURN_TRIP_POSSIBLE", "NO_RETURN_TRIP", "RECHARGE_NEEDED"]
instructions = ["No solar recharge is needed.", "Solar recharge is needed on the way back.", "Solar recharge is needed."]
code = 0

# Inputs
angle = float(input("Enter the angle in degrees: "))
travel_time = abs(float(input("Enter the travel time in seconds: ")))

# Calculations
distance = speed * travel_time
horizontal_distance = round(distance * math.sin(math.radians(angle)), 2)
vertical_distance = round(distance * math.cos(math.radians(angle)), 2)
estimated_battery_usage = travel_time * battery_usage
battery -= estimated_battery_usage

# Outputs
print("\nThe angle is: ", angle, "degrees")
print("The travel time is: ", travel_time, "s")
print("The distance travelled is: ", distance, "m")
print("The horizontal distance travelled is: ", horizontal_distance, "m")
print("The vertical distance travelled is: ", vertical_distance, "m")
print("The estimated battery usage is: ", estimated_battery_usage)
print("The battery is at: ", battery, "%.")

# Check if rover can travel the distance
if battery < 0:
    print("The battery is not enough to travel the distance. Solar recharge is needed.")
    code = 2
else:
    if battery > estimated_battery_usage:
        print("The battery is enough to travel back to the starting point. No solar recharge is needed.")
        code = 0
    else:
        print("The battery is not enough to travel back to the starting point. Solar recharge is needed on the way back.")
        code = 1
status = status[code]
instructions = instructions[code]
   
# Print Rover status
print("\n============================ ROVER STATUS ============================")
print("Position: X:", horizontal_distance, "Y:", vertical_distance)
print("Battery used: ", estimated_battery_usage, "%/s")
print("Current Battery: ", battery, "%")
print("Remaining distance until battery died: ", round(battery/battery_usage * speed, 2), "m")
print("Trip status: ", status)
print("Instructions: ", instructions)
print("======================================================================")

'''
TEST TABLE
# Actual result
=====================================================================================================================================================
# | Angle | Travel Time |  Distance  | Horizontal Distance | Vertical Distance | Estimated Battery Usage | Remaining Battery |        Status        |
=====================================================================================================================================================
1 |   0   |     10      |    15.0    |        0.0          |       15.0        |         27.0            |       73.0        | RETURN_TRIP_POSSIBLE |
2 |   0   |     15      |    22.5    |        0.0          |       22.5        |         40.5            |       59.5        | RETURN_TRIP_POSSIBLE |
3 |  45   |     20      |    30.0    |       21.21         |       21.21       |         54.0            |       46.0        | NO_RETURN_TRIP       |
4 |  45   |     30      |    45.0    |       31.82         |       31.82       |         81.0            |       19.0        | NO_RETURN_TRIP       |
5 |  90   |     40      |    60.0    |       60.0          |        0.0        |         108.0           |       -8.0        | MID_RECHARGE_NEEDED  |
=====================================================================================================================================================

# Expected result
=====================================================================================================================================================
# | Angle | Travel Time |  Distance  | Horizontal Distance | Vertical Distance | Estimated Battery Usage | Remaining Battery |        Status        |
=====================================================================================================================================================
1 |   0   |     10      |    15      |          0          |        15         |           27            |        73         | RETURN_TRIP_POSSIBLE |
2 |   0   |     15      |    22      |          0          |       22.5        |          40.5           |       59.5        | RETURN_TRIP_POSSIBLE |
3 |  45   |     20      |    30      |        21.21        |       21.21       |           54            |        46         | NO_RETURN_TRIP       |
4 |  45   |     30      |    45      |        31.82        |       31.82       |           81            |        19         | NO_RETURN_TRIP       |
5 |  90   |     40      |    60      |         60          |         0         |          108            |        -8         | MID_RECHARGE_NEEDED  |
=====================================================================================================================================================

# Test results
====================
# | Comment        |
====================
1 | Pass           |
2 | Pass           |
3 | Pass           |
4 | Pass           |
5 | Pass           |
====================

'''