"""
03. Practice: Data Types and Variables
Tasks
1. Create variables for name, age, and student status.
2. Print one sentence using all variables.
3. Ask for two numbers and print:
    - The sum (x + y)
    - The difference (x - y)
    - The product (x * y)
Convert "42" to an integer and add 8
"""
name = "Alex"
age = 56
is_student = True
print(f"{name} is {age} years old and student status is {is_student}.")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print(f"Sum: {x + y:f}")
print(f"Difference: {x - y:.3f}")
print(f"Product: {x * y:.2f}")
converted_number = int("42") + 8
print(f"Converted number: {converted_number}")
