def parallelogram_area(base, height):
    area = base * height
    return area

# Get input from the user
base = float(input("Enter the length of the base: "))
height = float(input("Enter the height: "))

# Calculate the area of the parallelogram
area = parallelogram_area(base, height)

# Display the result
print(f"The area of the parallelogram is: {area}")
