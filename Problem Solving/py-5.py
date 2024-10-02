#py-5.py 
"""
Write a Python program to input radius 
of a circle from user and find diameter, 
circumference and area of the circle. 
How to calculate diameter, circumference and 
area of a circle whose radius is given 
by user in Python programming. Logic to find diameter,
circumference and area of a circle in Python.

Input
Enter radius: 10

Output
Diameter = 20 units
Circumference = 62.79 units

"""

radius = int(input("Enter radius: "))

diameter = 2 * radius 
circumference = 2 * 3.1416 * radius
area = 3.1416 * radius * radius



print("Diameter = " + str(diameter) + " units")
print("circumference = " + str(circumference) + " units")
print("Area = " + str(area) + " sq. units")