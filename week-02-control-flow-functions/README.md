# Contents
- [02-01-05. Reflection: Conditionals](#02-01-05-reflection-conditionals)
  - [Recall Questions](#recall-questions)
  - [Micro Reflection](#micro-reflection)
- [Additional Reflection: Different Ways to Control a while Loop](#additional-reflection-different-ways-to-control-a-while-loop)
  - [1. while True + break](#1-while-true--break)
  - [2. Controlling the Loop with a State Variable](#2-controlling-the-loop-with-a-state-variable)
  - [3. Using a Condition Directly in the while Statement](#3-using-a-condition-directly-in-the-while-statement)
  - [4. Using return to Exit the Loop](#4-using-return-to-exit-the-loop)
  - [5. Using a Ternary Expression for Menu Logic](#5-using-a-ternary-expression-for-menu-logic)
  - [Conclusion Loops](#conclusion-loops)
  - [Lambda function](lambda-function)


## 02-01-05. Reflection: Conditionals

### Recall Questions

1. What is the difference between `if` and `elif`?
2. Why do we use `==` in conditions?
3. Why is input conversion important for numeric checks?

Skillnaden mellan if och elif:<br>
`if` är första villkoret och kontrolleras alltid. <br>
`elif` testas bara om föregående villkor var falskt. Det används för flera alternativa villkor i samma beslut.

Varför använder vi `==` i villkor?<br>
`==` jämför värden. `=` används för tilldelning. I en villkorssats måste vi jämföra, inte tilldela.

Varför är typomvandling av input viktig vid numeriska kontroller?<br>
`input()` returnerar alltid en sträng. För att kunna jämföra eller räkna med tal måste värdet omvandlas till t.ex. int eller float.


## Micro Reflection

Write 3–4 lines:

- One conditional bug I made this week.
- Why it happened (type issue, wrong operator, or indentation).
- How I fixed it.
- One rule I will use next time.

This week I experimented with two ways of reading numbers: a for loop and a list comprehension.

Loop version:
```
for n in range(3):
    list1.append(int(input(f"Enter n{n}: ")))
```

List comprehension version:
```
list1 = [int(input(f"Enter n{n}: ")) for n in range(3)]
```
The bug appeared when the user pressed Enter without typing a number.
input() returned '', and int('') or float('') raised a ValueError.
Both versions crashed for the same reason - I converted user input before validating it. The issue was not the loop or the list comprehension itself, but missing input validation before type conversion.<br>
Example of the error:
```
if just Enter, then  
    list1 = [float(input(f"Enter n{n}: ")) for n in range(N)]
             ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: ''
```
I fixed it by separating validation from conversion and handling errors explicitly:
```
for n in range(3):
    while True:
        try:
            value = int(input(f"Enter n{n}: "))
            list1.append(value)
            break
        except ValueError:
            print("Invalid input. Try again.")
```

Next time I will always validate user input before converting types and avoid combining input, validation, and conversion in a single expression.

I also experimented with lambda expressions for validation, but this reduced readability and made debugging harder.

Olicka varianter med Three numbers funktion:
```
# 2. Three numbers
def three_num():
    print("> Numbers (n1-nx) game.")
    #N = (lambda x: int(x) if x else 3)(input("> Enter amount (default 3): "))
    N = int( input("> Enter amount (default 3): ") or 3 )
    
    get_num = lambda n: (lambda x: float(x) if x else 0.0)(input(f"Enter n{n}: "))
    list1 = [get_num(n) for n in range(N)]
    
    print(f"Max: {max(list1)} / Min: {min(list1)} / Avg: {sum(list1)/N:.3f}")
```

```
# 2. Three numbers
def three_num():
    list1 = []
    print("> Three numbers (n1-n3) game.")
    for n in range(3):
        list1.append( int(input(f"Enter n{n}: ")) )
    print (f"Max: {max(list1)} / Min: {min(list1)} / Avg: {sum(list1)/3:.3f} \n")
```
<hr>

[↑ Contents](#contents)

# Additional Reflection: Different Ways to Control a `while` Loop

While working on my menu system and input validation, I explored several ways to control a while loop. I realized that there are multiple valid approaches, each with different implications for readability and structure.

### 1. while True + break

This approach uses an infinite loop and exits explicitly with break.

It is useful for repeated input validation because the loop continues until valid data is entered. The exit condition is handled inside the loop body. However, the termination logic is not visible in the loop header.

### 2. Controlling the Loop with a State Variable

In my menu implementation, I used a boolean variable:
```
menu = True
while menu:
    ...
    menu = False if choice == "4" else True
```
Here, the loop condition is controlled explicitly through a variable. This makes the state of the program clearer and separates the exit logic from break. I found this approach easier to reason about when building a small menu system.

### 3. Using a Condition Directly in the while Statement

Another clean option is:
```
choice = ""
while choice != "4":
    choice = input("Choice: ")
```
This makes the termination condition visible at the top of the loop, which improves readability and reduces the need for extra state variables.

### 4. Using `return` to Exit the Loop
When the loop is inside a function, it is possible to exit using `return`:
```
def main():
    while True:
        choice = input("Choice: ")
        if choice == "4":
            return
```
This simplifies control flow because the function ends immediately, and no additional flags are needed.

### 5. Using a Ternary Expression for Menu Logic

I also experimented with using nested ternary expressions inside the loop:
```
(
    show_menu() if choice == "0" else
    grade_checker() if choice == "1" else
    ...
)
```
Although this approach works and keeps the code compact, it reduces readability and becomes harder to debug as the program grows. It combines branching logic and function calls into a single expression, which is not typical Python style.

### Conclusion Loops

I learned that controlling a while loop can be done in several valid ways:

- break provides local control inside the loop.
- A state variable provides explicit and structured control.
- A direct condition in the loop header improves clarity.
- return simplifies exit logic inside functions.
- Ternary expressions can work but may reduce readability.

The key insight is that loop control is not just about syntax. It affects program structure, readability, and maintainability. Choosing the right approach depends on context and complexity.

[↑ Contents](#contents)

## Lambda function

### Switch/Case emulator 

```
def calc(op, x, y):
    return {
        '+': lambda: x + y,
        '-': lambda: x - y,
        '*': lambda: x * y,
        '/': lambda: x / y,
    }.get(op, lambda: None)()
    
print(calc("*", 8, 9))
```
