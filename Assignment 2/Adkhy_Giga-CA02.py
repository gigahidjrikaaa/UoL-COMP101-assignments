# Adkhy_Giga 201847335  October2024 CA-02.py
# Finding out if a rover can return to its starting point after travelling a certain time and angle

import math

speed = 1.5         # Speed in m/s
battery = 100       # Battery in percentage
battery_usage = 2.7 # Battery usage in percentage per second
status = ["RETURN_TRIP_POSSIBLE", "NO_RETURN_TRIP", "MID_RECHARGE_NEEDED"]       # Status of the travel

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
    print("The battery is not enough to travel the distance.")
    print("Solar recharge is needed.")
    status = status[2]
else:
    if battery > estimated_battery_usage:
        print("The battery is enough to travel back to the starting point. No solar recharge is needed.")
        status = status[0]
    else:
        print("The battery is not enough to travel back to the starting point. Solar recharge is needed on the way back.")
        status = status[1]
   
# Rover status
print("\n============================ ROVER STATUS ============================")
print("Position: X:", horizontal_distance, "Y:", vertical_distance)
print("Battery: ", battery, "%")
print("Remaining distance until battery died: ", round(battery/battery_usage * speed, 2), "m")
print("Status: ", status)
print("======================================================================")

'''
Test Table
=============================================================================================================================================================================================
| Angle | Travel Time |  Distance  | Horizontal Distance | Vertical Distance | Estimated Battery Usage | Remaining Battery |    Actual Status     |    Expected Status   |     Comments     |
=============================================================================================================================================================================================
|   0   |     10      |    15.0    |        0.0          |       15.0        |         27.0            |       73.0        | RETURN_TRIP_POSSIBLE | RETURN_TRIP_POSSIBLE |  PASS            |
|   0   |     20      |    30.0    |        0.0          |       30.0        |         54.0            |       46.0        | NO_RETURN_TRIP       | NO_RETURN_TRIP       |  PASS            |
|  45   |     20      |    30.0    |       21.21         |       21.21       |         54.0            |       46.0        | NO_RETURN_TRIP       | NO_RETURN_TRIP       |  PASS            |
|  45   |     30      |    45.0    |       31.82         |       31.82       |         81.0            |       19.0        | NO_RETURN_TRIP       | NO_RETURN_TRIP       |  PASS            |
|  90   |     40      |    60.0    |       60.0          |        0.0        |         108.0           |       -8.0        | MID_RECHARGE_NEEDED  | MID_RECHARGE_NEEDED  |  PASS            |
=============================================================================================================================================================================================

'''