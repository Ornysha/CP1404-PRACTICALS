# 1. Write user's name to a file
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from the file
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}")

# 3. Read first two numbers from numbers.txt
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    total = first_number + second_number
print(total)

# 4. Sum all numbers in numbers.txt
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
print(total)
