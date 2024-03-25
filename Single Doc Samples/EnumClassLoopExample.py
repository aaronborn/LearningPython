from enum import Enum

# Define an enum for days of the week
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Define a class with a method
class Calculator:
    def add(self, a, b):
        return a + b

# Single-dimensional array (list in Python)
numbers = [1, 2, 3, 4, 5]

# Multi-dimensional array (list of lists in Python)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using the Calculator class
calc = Calculator()
sum = calc.add(10, 20)

# While loop
count = 0
while count < len(numbers):
    print(f"While loop, number: {numbers[count]}")
    count += 1

# For loop
print("\nFor loop, days of the week:")
for day in Weekday:
    print(f"{day.name}: {day.value}")

# Printing the sum
print(f"\nThe sum of 10 and 20 is {sum}")

# Printing the single-dimensional array
print("\nSingle-dimensional array:", numbers)

# Printing the multi-dimensional array
print("\nMulti-dimensional array:")
for row in matrix:
    print(row)

# Using a list
fruits = ["apple", "banana", "cherry"]
print("\nList of fruits:", fruits)
