# Skillnaden mellan booleska värden i Python och JavaScript

## 1. Skrivsätt

Booleska värden – Python vs JavaScript

| Egenskap | Python | JavaScript |
|-----------|-----------|---------------|
| Bool-värden | `True` / `False` | `true` / `false` |
| Skiftläge | Börjar med stor bokstav | Skrivs med liten bokstav |
| Typ | Objekt av typen `bool` | Primitiv typ |
| Case-sensitive | --- Ja --- | --- Ja --- |

---

### Kodexempel

| Python | JavaScript |
|--------|------------|
| `True False` | `true false` |

---

**Observera:**  
Båda språken är skiftlägeskänsliga (case-sensitive). Fel bokstavsstorlek leder till fel.

------------------------------------------------------------------------

## 2. Typomvandling (boolean conversion)
**Python -- mer förutsägbart**<br>
Python använder en tydlig och konsekvent logik för vad som räknas som `False`.

| Python | JavaScript |
|--------|------------|
|`bool(0)  #False`|`Boolean(0)        //false`|
|`bool("") #False`|`Boolean("")       //false`|
|`bool([]) #False`|`Boolean(null)     //false`|
| `--- ` | `Boolean(undefined)//false`|



### JavaScript -- truthy / falsy

Men i JavaScript:

```
Boolean("0")      // true
Boolean([])       // true
Boolean({})       // true

```

JavaScript har fler implicita (automatiska) typomvandlingar, vilket kan
skapa oväntat beteende.

## Boolean conversion – Python vs JavaScript

| Värde | Python | JavaScript | Kommentar |
|--------|-----------|---------------|-------------|
| `0` | `False` | `false` | Båda tolkar 0 som falskt |
| `1` | `True` | `true` | Alla icke-nolltal är sanna |
| `""` (tom sträng) | `False` | `false` | Tom sträng är falsk |
| `"0"` | `True` | `true` | Icke-tom sträng är sann |
| `"false"` | `True` | `true` | Strängvärden är alltid sanna om de inte är tomma |
| `[]` (tom lista/array) | `False` | `true` | Viktig skillnad |
| `{}` (tom dict/objekt) | `False` | `true` | Viktig skillnad |
| `None` / `null` | `False` | `false` | Båda tolkar som falskt |
| `undefined` | – | `false` | Finns bara i JavaScript |

**Viktig skillnad**

I Python är tomma datastrukturer falska:
```
bool([])      # False
bool({})      # False
```

I JavaScript är tomma objekt och arrayer sanna:
```
Boolean([])   // true
Boolean({})   // true
```

Detta är en av de mest praktiska skillnaderna mellan språken.

------------------------------------------------------------------------

### Sammanfattande regel

Python
```
0 → False
Tomma strukturer → False
None → False
Allt annat → True
```
JavaScript
```
0 → false
"" → false
null → false
undefined → false
NaN → false
Tomma objekt/arrayer → true
```

------------------------------------------------------------------------

## 3. Jämförelseoperatorer

Python
```
if x == True:
# Det finns endast en typ av likhetsjämförelse (`==`).
```

JavaScript har två jämförelseoperatorer:
```
if (x === true) {
}
// ==   med typomvandling\
// ===  strikt jämförelse (rekommenderas)

```



------------------------------------------------------------------------

### Sammanfattning

 | Python                        | JavaScript |
 | ------------------------------| ----------------------------------|
 | `True` / `False`              | `true` / `false` |
 | Bool är objekt                | Bool är primitiv typ |
 | Förutsägbar typomvandling     | truthy / falsy-logik |
 | En jämförelse (`==`)  | Två jämförelser (`==` och `===`) |



## Slutsats

Python har en mer strikt och förutsägbar hantering av booleska värden.\
JavaScript är mer flexibel, men kan kräva större uppmärksamhet kring
typomvandling och jämförelser.
