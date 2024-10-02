
"""

Write a Python program to input two numbers from user 
and find their power using pow function. 
How to find power of a number in Python programming.
 How to use pow function in Python programming.

Input
Enter base: 5
Enter exponent: 2

Output
5 ^ 2 = 25

pow() = power 


"""

base = int(input("Enter base:"))
exponent = int(input("Enter exponent:"))

power = pow(base, exponent)

print("%d ^ %d = %d" %(base, exponent, power))