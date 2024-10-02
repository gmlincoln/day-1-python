"""
Write a Python program to input length in centimeter and convert it to meter and kilometer. How to convert length from centimeter to meter and kilometer in Python programming. Length conversion program in Python from centimeter to meter and centimeter to kilometer.
Input
Enter length in centimeter = 1000
Output
Length in meter = 10 m
Length in kilometer = 0.01 km

1m = 100cm
1km = 1000m
1km = 1000 *1m
1km = 1000 * 100cm


"""

centimeter = int(input("Enter centimeter = "))

meter = centimeter / 100

kilometer = meter / 1000

print("Length in meter = " + str(meter) +" m")
print("Length in kilometer = " + str(kilometer) +" km")

