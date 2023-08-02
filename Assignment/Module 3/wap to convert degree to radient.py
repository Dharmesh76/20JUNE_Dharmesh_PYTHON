import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# Get input from the user
degrees = float(input("Enter degrees: "))

# Convert degrees to radians
radians = degrees_to_radians(degrees)

# Display the result
print(f"{degrees} degrees is equal to {radians} radians.")
