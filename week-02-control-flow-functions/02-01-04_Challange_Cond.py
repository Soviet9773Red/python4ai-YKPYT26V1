# 02-01-04 Challenge: Conditionals
"""
1. Build a small grade checker for scores from 0 to 100.
2. Ask for three numbers and print the largest.
3. Ask for a year and print whether it is a leap year (basic rule only: divisible by 4).
"""

#1. Grade checker 1-100
def grade_checker():
    print("Grade checker game.")
    grade = int(input("> Enter your grade (0 - 100): "))
    res = (
        "wrong input!\n" if (grade < 0 or grade > 100) else
        "Newbie\n" if grade < 20 else
        "Rookie\n" if grade < 40 else
        "Talented\n" if grade < 55 else
        "Skilled\n" if grade < 70 else
        "Advanced\n" if grade < 95 else
        "Expert\n"
    )
    print("> Your level is: " + res if res!="wrong input!\n" else res)

# 2. Three numbers
def three_num():
    print("> Numbers (n1-nx) game.")
    #N = (lambda x: int(x) if x else 3)(input("> Enter amount (default 3): "))
    N = int( input("> Enter amount (default 3): ") or 3 )
    
    get_num = lambda n: (lambda x: float(x) if x else 0.0)(input(f"Enter n{n}: "))
    list1 = [get_num(n) for n in range(N)]
    
    print(f"Max: {max(list1)} / Min: {min(list1)} / Avg: {sum(list1)/N:.3f}")

# 3. Leap year
    # Every year that is exactly divisible by four is a leap year, 
    # except for years that are exactly divisible by 100, 
    # but these centurial years are leap years, if they are exactly divisible by 400.
    # For example, the years 1700, 1800, and 1900 were not leap years, but the years 1600 and 2000 were.
def leap_y():
    print("> Leap year game")
    y = int(input("Take a leap! Enter year: "))   
    print("This year is leap"
          if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) else 
          "This year not leap")

# 0. Show menu
def show_menu():
    print(
        "\n0. Show menu.\n============\n"
        "1. Grade checker\n"
        "2. Three numbers game\n"
        "3. Leap year calculator\n"
        "4. Exit\n"
    )

def main():
    show_menu()
    menu = True
    while menu:

        choice = input("0. Show menu:> ")

        (
            show_menu() if choice == "0" else
            grade_checker() if choice == "1" else
            three_num() if choice == "2" else
            leap_y() if choice == "3" else
            print("> Exiting ...") if choice == "4" else
            print("> Invalid input") 
        )
        print()  # empty line
        menu = False if choice == "4" else True

main()
