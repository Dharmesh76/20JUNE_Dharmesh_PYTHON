def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

# Get input from the user
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height: "))

# Calculate the area of the trapezoid
area = trapezoid_area(base1, base2, height)

# Display the result
print(f"The area of the trapezoid is: {area}")
