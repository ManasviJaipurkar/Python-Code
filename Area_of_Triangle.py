# Two method's for finding area of triangle

# Get input from the user
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
area = 0.5 * base * height

# Display the result
print(f"The area of the triangle is: {area}")



import math

# Get input from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Display the result
print(f"The area of the triangle is: {area}")






