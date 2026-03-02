value = input("Enter a number: ")
number = int(value)
print(type(value))
print(type(number))
"""
# wrong value for int
value = "3.14"
number = int(value)
print(number)
"""
value = "3.14"
try:
    number = int(value)
except ValueError:
    number = int(float(value))
print(number)

"""
try:
    # risky code
except ValueError:
    # handle specific error
except TypeError:
    # handle another error
else:
    # runs if no error
finally:
    # runs always
"""