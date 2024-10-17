# Adkhy_Giga 201847335  October2024 CA-02.py
# A

min_angle = 0       # Minimum angle in degrees (North)
max_angle = 90      # Maximum angle in degrees (East, inclusive)
speed = 1.5         # Speed in m/s
battery = 100       # Battery in percentage
battery_usage = 2.7 # Battery usage in percentage per second

# Inputs
angle = float(input("Enter the angle in degrees: "))
travel_time = float(input("Enter the travel time in seconds: "))

# Calculations
distance = speed * travel_time
horizontal_distance = distance * (angle / max_angle)
vertical_distance = distance * ((max_angle - angle) / max_angle)
estimated_battery_usage = travel_time * battery_usage

# Outputs
print("\nThe angle is: ", angle)
print("The travel time is: ", travel_time)

# Check if robot can travel the distance
if estimated_battery_usage > battery:
    print("The robot has travelled", horizontal_distance, "m horizontally and", vertical_distance, "m vertically. Total distance travelled is", distance, "m.")
    print("The battery is not enough to travel the distance.")
else:
    print("The robot has travelled", horizontal_distance, "m horizontally and", vertical_distance, "m vertically. Total distance travelled is", distance, "m.")
    print("The battery is at", battery - estimated_battery_usage, "%.")
    if battery - estimated_battery_usage > estimated_battery_usage:
        print("The battery is enough to travel back to the starting point. No solar recharge is needed.")
    else:
        print("The battery is not enough to travel back to the starting point. Solar recharge is needed.")
        

