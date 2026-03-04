
## 02-01-05. Reflection: Conditionals

### Recall Questions

1. What is the difference between `if` and `elif`?
2. Why do we use `==` in conditions?
3. Why is input conversion important for numeric checks?

Skillnaden mellan if och elif:<br>
if är första villkoret och kontrolleras alltid. <br>
elif testas bara om föregående villkor var falskt. Det används för flera alternativa villkor i samma beslut.

Varför använder vi == i villkor?<br>
== jämför värden. = används för tilldelning. I en villkorssats måste vi jämföra, inte tilldela.

Varför är typomvandling av input viktig vid numeriska kontroller?<br>
input() returnerar alltid en sträng. För att kunna jämföra eller räkna med tal måste värdet omvandlas till t.ex. int eller float.


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
