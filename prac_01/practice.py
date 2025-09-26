import random
high_number = int(input("Enter the high number: "))
low_number = int(input("Enter the low number: "))
while low_number >= high_number:
     print("Invalid input")
     low_number = int(input("Enter the low number: "))
# print(low_number, high_number)
print(random.randint(low_number, high_number))
