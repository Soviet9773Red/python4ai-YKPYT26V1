"""
01_04_04 Challenge: Data Types and Variables

1. Ask for item price and tax rate, then calculate the total price.
2. Build a simple BMI calculator using user input.
3. Ask for exam points and max points, then print the percentage.
"""

# Challenge 1: Total Price Calculator
print("Challenge 1: Total Price Calculator")
item_price = float(input("Enter the item price: "))
tax_rate = float(input("Enter the tax rate (%): "))
total_price = item_price + (item_price * tax_rate / 100)
print(f"Total price including tax: ${total_price:.2f}\n")

# Challenge 2: BMI Calculator
print("Challenge 2: BMI Calculator")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")
results = "Underweight" if bmi <= 18.5 else "Normal weight" if bmi <= 25 else "Overweight" if bmi <= 30 else "Obesity"
print(f"Your BMI category is: {results}\n")

# Challenge 3: Exam Percentage Calculator
print("Challenge 3: Exam Percentage Calculator")
exam_points = float(input("Enter the points you scored on the exam: "))
max_points = float(input("Enter the maximum points possible: "))
percentage = (exam_points / max_points * 100) if max_points > 0 else 0
print(f"Your exam percentage is: {percentage:.2f}%")
