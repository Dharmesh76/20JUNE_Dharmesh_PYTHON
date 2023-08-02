import math

def calculate_cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def calculate_cylinder_surface_area(radius, height):
    base_area = math.pi * radius**2
    lateral_area = 2 * math.pi * radius * height
    surface_area = 2 * base_area + lateral_area
    return surface_area

def main():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))

    volume = calculate_cylinder_volume(radius, height)
    surface_area = calculate_cylinder_surface_area(radius, height)

    print(f"The volume of the cylinder is: {volume:.2f} cubic units")
    print(f"The surface area of the cylinder is: {surface_area:.2f} square units")

if __name__ == "__main__":
    main()
