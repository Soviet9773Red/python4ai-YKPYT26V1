#02-01-03 Practice: Conditionals
"""
TODO
1. Ask for temperature and print Cold, Warm, or Hot.
2. Ask for a number and print whether it is even or odd.
3. Ask for username and password and print Login success only if both are correct.
4. Ask for age and print whether the user can vote (18 or older).
5. Ask for exam score and print grade level (A, B, C, F) using simple ranges.
6. Ask for two numbers and print which one is larger. If equal, print Same value.
7. Predict output before running:
    x = 12
    if x > 10:
        print("A")
    if x > 15:
        print("B")
    else:
        print("C")
    # Answer: A , C  due to second if is non elif
"""
# 1.
t = int(input("Enter the temperatue in °C: "))
print("Cold" if t<18 else "Warm" if t>=18 and t<25 else "Hot")
# 2.
n = int(input("Enter integer number: "))
print("Odd number" if n%2 !=0 else "Even number")
# 3.
l, p = input("Enter Login(admin) and Password (qwertz) separated by by space: ").split()
print("Acces granted!" if (l == "admin" and p == "qwertz") else "Acces denyed!")
# 4.
age = int(input ("Your age? :"))
print("You can vote!" if age >=18 else "Sorry , you can not vote.")
# 5.
score = int(input("Enter your exam score (50 - 120): "))
res = (
    "A" if score >= 50  and score <   60 else
    "B" if score >= 60  and score <   80 else
    "C" if score >= 80  and score <  100 else
    "F" if score >= 100 and score <= 120 else
    "wrong score!"
    )
print("Your grade level is: " + res if len(res)==1  else res)
# 6. 
try:
    n1, n2 = input("Enter two comma-separated numbers (n1, n2): ").split(',')
    n1, n2 = int(n1.strip()), int(n2.strip()) # delete all spaces 
    print(
        f"{n1} > {n2}" if int(n1)>int(n2) else
        f"{n2} > {n1}" if int(n2)>int(n1) else
        f"{n2} = {n1}"
    )
except:
    print("Wrong input")