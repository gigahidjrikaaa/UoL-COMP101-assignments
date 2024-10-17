# Adkhy_Giga 201847335  October2024 CA-02.py
# A

import math

speed = 1.5         # Speed in m/s
battery = 100       # Battery in percentage
battery_usage = 2.7 # Battery usage in percentage per second
status = {"RETURN_TRIP", "ONE_TRIP", "MID_RECHARGE_NEEDED"}       # Status of the travel

# Inputs
angle = float(input("Enter the angle in degrees: "))
travel_time = float(input("Enter the travel time in seconds: "))

# Calculations
distance = speed * travel_time
# Horizontal distance travelled: distance multiplied by the sine of the angle
horizontal_distance = distance * math.sin(math.radians(angle))
# Vertical distance travelled: distance multiplied by the cosine of the angle
vertical_distance = distance * math.cos(math.radians(angle))
estimated_battery_usage = travel_time * battery_usage

# Outputs
print("\nThe angle is: ", angle)
print("The travel time is: ", travel_time)
print("The distance travelled is: ", distance)
print("The horizontal distance travelled is: ", horizontal_distance)
print("The vertical distance travelled is: ", vertical_distance)
print("The estimated battery usage is: ", estimated_battery_usage)
print("The battery is at: ", battery - estimated_battery_usage, "%.")

# Check if robot can travel the distance
if battery - estimated_battery_usage < 0:
    print("The battery is not enough to travel the distance.")
    print("Solar recharge is needed.")
else:
    if battery - estimated_battery_usage > estimated_battery_usage:
        print("The battery is enough to travel back to the starting point. No solar recharge is needed.")
    else:
        print("The battery is not enough to travel back to the starting point. Solar recharge is needed.")
   

