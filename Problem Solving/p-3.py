"""
Write a Python program to input length and width
of a rectangle and calculate perimeter of the rectangle. 
How to find perimeter of a rectangle in Python programming. 
Logic to find the perimeter of a rectangle if length 
and width are given in Python programming.

Input
Enter length: 5
Enter width: 10
Output


"""

length, width = map(int, input("Enter length and width = ").split())

perimeter = 2 * (length + width)

print("Perimeter = ", perimeter)