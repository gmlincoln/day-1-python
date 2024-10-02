"""
Write a Python program to input number of days 
from user and convert it to years, weeks and days. 
How to convert days to years, months and weeks in Python programming. 
Logic to convert days to years, months and 
weeks in Python program.

1yr  = 365 days

1month = 30 days

1week = 7 days


Input
Enter days: 373
Output
365days = 1 year, 1 week and 1 day


"""

days = int(input("Enter days = "))

year = days / 365

month = days / 30

week = days // 7

print("Year = ", int(year))
print("Months = ", int(month))
print("Weeks = ", week)


