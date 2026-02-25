"""
Build a short profile collector (name, age, country, favorite topic) and print a 2-line summary.
Ask for temperature in Celsius and print a rough Fahrenheit conversion.
Ask for three numbers and print their average.
"""
Info = " neurothrone / python-for-aipython-for-ai / week-01-intro-python-ai / 03-input-output / 04-challenge.md\n"
Menu = (
    "\nChallenge 04\n"
    "Select the task:\n"
    "1. Profile Collector\n"
    "2. Temperature Converter\n"
    "3. Average Calculator\n"
    "4. Exit"
)

def print_menu():
    print(Menu)

def profile_collector():
       print("Profile Collector")
       name = input("Name? ")
       age = int(input("Age? "))
       country = input("Country? ")
       favorite_topic = input("Favorite topic? ")
       print(f"Name: {name}, Age: {age}")
       print(f"Country: {country}, Favorite topic: {favorite_topic}")
       

def temperature_converter():
    print("\nTemperature Converter")
    celsius = float(input("Temperature in Celsius? ")) 
    fahrenheit = celsius * 9/5 + 32
    print(f"Temperature in Fahrenheit: {fahrenheit}")
    

def average_calculator():
    print("\nAverage Calculator")
    num1 = float(input("First number? "))
    num2 = float(input("Second number? "))
    num3 = float(input("Third number? "))
    average = (num1 + num2 + num3) / 3
    print(f"Average: {average:.2f}")
    

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            profile_collector()
        elif choice == "2":
            temperature_converter()
        elif choice == "3":
            average_calculator()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

print(Info)
main()




