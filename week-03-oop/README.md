
# OOP Basics

Iteration, iteratorer och objekt i Python
1. Grundidé
I Python är nästan allt ett objekt.

Det gäller även strukturer som listor, funktioner, generatorer och iteratorer.
När man skriver kod som
```
for x in data:
    print(x)
```
använder Python i själva verket en generell mekanism som kallas iteration protocol.
Denna mekanism gör det möjligt att gå igenom element i ett objekt ett i taget.
________________________________________
2. Iterationsprotokollet i Python
Ett objekt kan itereras om det implementerar två speciella metoder:
```
__iter__()
__next__()
```
Dessa metoder kallas special methods (eller dunder methods eftersom de har dubbel underscore).

```iter()```
Returnerar en iterator.

```next()```
Returnerar nästa element i sekvensen.

Om det inte finns fler element kastas ett undantag:
```StopIteration```
________________________________________
3. Vad händer i en for-loop

När Python kör

```for x in obj:```

sker följande steg internt:

Python anropar
```obj.__iter__()```

Den returnerade iteratorn används för att hämta element:
```iterator.__next__()```

Varje värde tilldelas variabeln x.

När StopIteration uppstår avslutas loopen.
________________________________________
4. Exempel på en egen iterator
   ```
class Counter:

    def __init__(self, max):
        self.current = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= self.max:
            raise StopIteration

        self.current += 1
        return self.current
        ```
Användning:
```
for x in Counter(5):
    print(x)
```
Resultat:
```
1
2
3
4
5
```
________________________________________

5. Iteratorer i standardbiblioteket

Många funktioner i Python returnerar iteratorer istället för listor.

Exempel:
```
range()
filter()
map()
zip()
```

Till exempel:
```
f = filter(is_prime, range(100))
```

filter() returnerar inte en lista utan ett filter-objekt, som är en iterator.
Om man skriver
```
print(f)
```

får man
```
<filter object at 0x...>
```

Detta är bara objektets representation i minnet.

________________________________________

6. Lazy evaluation

Iteratorer arbetar ofta med något som kallas lazy evaluation.
Det betyder att värden inte beräknas förrän de verkligen behövs.

Exempel:
```
list(f)
```

När list() körs börjar Python faktiskt iterera genom filter-objektet och samla resultaten.

________________________________________

7. Iteratorer är engångsobjekt

En viktig egenskap är att iteratorer normalt kan användas bara en gång.

[Exempel:](https://github.com/Soviet9773Red/python4ai-YKPYT26V1/blob/main/python-for-ai/week-03-oop/PrimeNumber.py) 
```
f = filter(is_prime, range(10))

print(list(f))
print(list(f))
```

Resultat:
```
[2, 3, 5, 7]
[]
```

Efter första iterationen är iteratorn redan förbrukad.
________________________________________

8. Sambandet mellan objekt och iteration

Iteration i Python är direkt kopplad till objektmodellen.

Många operationer i Python använder specialmetoder:

| operation | metod |
|-----------|-------|
| print(obj)| str__() 
| len(obj) | __len__() |
|obj[i]|__getitem__()|
|for x in obj|__iter__() + __next__()|

Detta gör att egna objekt kan bete sig som inbyggda datatyper.
________________________________________

9. Sammanfattning

Python använder ett enhetligt system för iteration.

Det bygger på:
- objekt
- specialmetoder
- iteratorer
- lazy evaluation
Detta gör språket flexibelt och minnes-effektivt.

________________________________________


varför Python använder iteratorer?

skillnaden mellan iterable och iterator ?

hur generatorer (yield) passar in i samma modell ?

OOP i Python, ==> (__iter__, __len__, __getitem__)
