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
        "Newbie\n" if grade >= 0  and grade <   20 else
        "Rookie\n" if grade >= 20  and grade <   40 else
        "Talented\n" if grade >= 40  and grade <   55 else
        "Skilled\n" if grade >= 55  and grade <   70 else
        "Advanced\n" if grade >= 70  and grade <  95 else
        "Expert\n" if grade >= 95 and grade <= 100 else
        "wrong input!\n"
        )
    print("> Your level is: " + res if res!="wrong input!"  else res)

# 2. Three numbers
def three_num():
    list1 = []
    print("> Three numbers (n1-n3) game.")
    for n in range(3):
        list1.append( int(input(f"Enter n{n}: ")) )
    print (f"Max: {max(list1)} / Min: {min(list1)} / Avg: {sum(list1)/3:.4f} \n")

# 3. Leap year
    # Every year that is exactly divisible by four is a leap year, 
    # except for years that are exactly divisible by 100, 
    # but these centurial years are leap years, if they are exactly divisible by 400.
    # For example, the years 1700, 1800, and 1900 were not leap years, but the years 1600 and 2000 were.
def leap_y():
    print("> Leap year game")
    y = int(input("Enter year to leap: "))   
    print("This year is leap\n"
          if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) else 
          "This year not leap\n")

# 0. Show menu
def show_menu():
    print(
        "\n0. Show menu.\n==========\n"
        "1. Grade checker\n"
        "2. Three numbers game\n"
        "3. Leap year calculator\n"
        "4. Exit\n"
    )

def main():
    show_menu()
    menu = True
    while menu:
        # print(
        #     "0. show menu > "
        # )
        choice = input("menu(0):> ")
        (
            show_menu() if choice == "0" else
            grade_checker() if choice == "1" else
            three_num() if choice == "2" else
            leap_y() if choice == "3" else
            print("> Exiting ...") if choice == "4" else
            print("> Invalid input") 
        )

        menu = False if choice == "4" else True


main()