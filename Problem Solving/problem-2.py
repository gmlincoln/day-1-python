"""
Write a Python program to input two numbers and 
perform all arithmetic operations. 
How to perform all arithmetic operation between two numbers 
in Python programming. 
Python program to find sum, difference, product, quotient and modulus
of two given numbers.
Input:
First number: 10
Second number: 5

sum / addition = 10 + 5 = 15
subtraction/difference = 10 - 5 = 5
multiplication/product = 10 * 5 = 50
quotient / division = 10 / 5 = 2 
modulus = 10 % 5 = 0 

"""

num_one, num_two = map(int, input("Enter two numbers separated by space: ").split())

sum = num_one + num_two 
print("Sum = ", sum)

subtraction = num_one - num_two
print("Subtraction = ", subtraction)

product = num_one * num_two
print("Product = ", product)


quotient = num_one / num_two
print("Quotient = ", quotient)

modulus =  num_one % num_two # 110 % 30 = 20
print("Modulus = ", modulus)


