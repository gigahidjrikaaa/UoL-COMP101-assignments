# Adkhy_Giga 201847335  October2024 CA-02.py
# A

import math

speed = 1.5         # Speed in m/s
battery = 100       # Battery in percentage
battery_usage = 2.7 # Battery usage in percentage per second
status = {"RETURN_TRIP_POSSIBLE", "NO_RETURN_TRIP", "MID_RECHARGE_NEEDED"}       # Status of the travel

# Inputs
angle = float(input("Enter the angle in degrees: "))
travel_time = float(input("Enter the travel time in seconds: "))

# Calculations
distance = speed * travel_time
# Horizontal distance travelled: distance multiplied by the sine of the angle
horizontal_distance = round(distance * math.sin(math.radians(angle)), 2)
# Vertical distance travelled: distance multiplied by the cosine of the angle
vertical_distance = round(distance * math.cos(math.radians(angle)), 2)
estimated_battery_usage = travel_time * battery_usage
battery -= estimated_battery_usage

# Outputs
print("\nThe angle is: ", angle)
print("The travel time is: ", travel_time)
print("The distance travelled is: ", distance)
print("The horizontal distance travelled is: ", horizontal_distance)
print("The vertical distance travelled is: ", vertical_distance)
print("The estimated battery usage is: ", estimated_battery_usage)
print("The battery is at: ", battery, "%.")

# Check if rover can travel the distance
if battery < 0:
    print("The battery is not enough to travel the distance.")
    print("Solar recharge is needed.")
    status = "MID_RECHARGE_NEEDED"
else:
    if battery > estimated_battery_usage:
        print("The battery is enough to travel back to the starting point. No solar recharge is needed.")
        status = "RETURN_TRIP"
    else:
        print("The battery is not enough to travel back to the starting point. Solar recharge is needed.")
        status = "ONE_TRIP"
   
# Rover status
print("\n============================ ROVER STATUS ============================")
print("Position: X:", horizontal_distance, "Y:", vertical_distance)
print("Battery: ", battery, "%")
print("Status: ", status)
print("Estimated distance without recharge: ", battery / battery_usage * speed, "m")
print("======================================================================")
