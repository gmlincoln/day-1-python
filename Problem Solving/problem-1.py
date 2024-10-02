#Write a Python program to input two numbers from user and calculate 
# their sum. 
# Python program to add two numbers and display their sum as output. 

#Input first number: 20
#Input second number: 10
#Sum = 30

# num_one = int(input("Enter a number = "))#10
# num_two = int(input("Enter an another number = ")) #20

# sum = num_one + num_two # 10 + 20 = 30

# print("Sum = ", sum)

 #map(type, "eeeeee".split())

# num_1 , num_2 = map(int, input("Enter two numbers: ").split())
# sum = num_1 + num_2 

# print("Sum =", sum)

numbers = list(map(int, input("Enter numbers separated by space= ").split()))

# print(type(numbers))

print(numbers)

# total = sum(numbers)

# print("Sum = ", total)

# [10, 20, 30, 40]

total = 0

for num in numbers:

    total += num #total = total + num # 0 + 10 = 10 # 10 + 20 = 30 .....100
    print("Inside for loop: ", total)

print("Outside for loop: ", total)

