"""
03 Practice: Input and Output
Tasks
Ask for a first name and last name, then print the full name.
Ask for two integers and print their sum.
Ask for a city and print a welcome message.
Ask for birth year and estimate current age.
"""
name = input("First name? ") + " " + input("Last name? ")
print(f"Full name: {name}")
 
summa  = int(input ("Two integers? Enter the first integer! ")) + int(input("Enter the second integer! "))
print(f"Sum: {summa}")
city = input("City? ")
print(f"Welcome to {city}!")
birth_year = int(input("Birth year? "))
from datetime import datetime
current_year = datetime.now().year
#current_year = 2026
age = current_year - birth_year
print(f"Estimated age: {age}")
print("All tasks completed!")
