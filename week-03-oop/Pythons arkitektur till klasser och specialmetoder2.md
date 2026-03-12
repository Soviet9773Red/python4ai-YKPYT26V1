Här är en sammanhängande och lugnt uppbyggd svensk version som binder ihop hela kedjan:

*   Pythons grundarkitektur
    
*   att allt är objekt
    
*   funktioner och variabler som objekt
    
*   specialmetoder
    
*   klasser
    
*   varför \_\_init\_\_, \_\_str\_\_, \_\_len\_\_, \_\_iter\_\_ och \_\_next\_\_ finns
    

Du kan använda texten både för egna anteckningar och som underlag i diskussion med läraren.

Från Pythons arkitektur till klasser och specialmetoder
=======================================================

1\. Grundidén i Python
----------------------

En av de viktigaste idéerna i Python är:

**nästan allt är objekt.**

Det betyder att värden, funktioner, listor, strängar och även klasser behandlas som objekt i språkets modell.

Exempel:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   x = 10text = "hej"nums = [1, 2, 3]   `

Alla dessa är objekt.

Vi kan kontrollera typen:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   print(type(x))print(type(text))print(type(nums))   `

Resultat:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML

Alltså: ett heltal i Python är inte bara "ett tal". Det är ett objekt av typen int.En sträng är ett objekt av typen str.En lista är ett objekt av typen list.

Detta är en viktig utgångspunkt, eftersom klasser inte är något främmande tillägg ovanpå Python. De växer naturligt fram ur samma modell.

2\. Objekt har data och beteende
--------------------------------

Ett objekt kan ha:

*   **attribut** - data som hör till objektet
    
*   **metoder** - funktioner som hör till objektet
    

Exempel med en sträng:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   text = "hello"print(text.upper())   `

Här är "hello" ett objekt, och upper() är en metod som tillhör det objektet.

Man kan säga att Python ofta arbetar enligt modellen:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   objekt.någonting   `

där någonting kan vara ett attribut eller en metod.

3\. Även funktioner är objekt
-----------------------------

I Python är även funktioner objekt.

Exempel:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   def add(a, b):    return a + bprint(type(add))   `

Resultat:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML

Det betyder att en funktion kan behandlas som ett vanligt objekt.Man kan till exempel lagra den i en variabel:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   f = addprint(f(2, 3))   `

Alltså är en funktion i Python inte bara "kod som körs". Den är också ett objekt som kan skickas runt, sparas och användas senare.

Detta är viktigt, eftersom det visar att Python har en ganska enhetlig arkitektur: samma objektidé gäller på många nivåer.

4\. Python-syntax är ofta bara en förenklad yta
-----------------------------------------------

När man börjar programmera ser det ofta ut som att Python har många separata "magiska" konstruktioner:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   print(x)len(nums)for n in nums:    print(n)   `

Men bakom denna syntax använder Python ofta objektens egna metoder.

Det innebär att språkets syntax ofta bara är ett bekvämt sätt att anropa särskilda metoder på objekt.

Det är här specialmetoderna kommer in.

5\. Specialmetoder
------------------

Specialmetoder är metoder med dubbla understreck före och efter namnet, till exempel:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   __init____str____len____iter____next__   `

De kallas ofta:

*   **special methods**
    
*   **dunder methods** ("double underscore")
    

De anropas ofta inte direkt av programmeraren, utan **automatiskt av Python** när man använder viss syntax.

Det är därför de är så viktiga: de kopplar ihop objekt med språkets inbyggda konstruktioner.

6\. \_\_init\_\_ - används när ett objekt skapas
================================================

När man skriver:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   class Dog:    def __init__(self, name):        self.name = namedog = Dog("Buddy")   `

då händer i princip detta:

1.  Python skapar ett nytt objekt
    
2.  Python anropar \_\_init\_\_ för att ge objektet sitt startläge
    

Man kan tänka ungefär så här:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Dog.__init__(dog, "Buddy")   `

\_\_init\_\_ används alltså för att **initiera objektet**, det vill säga ge det startvärden.

### Rollen av self

self är en referens till det aktuella objektet.

I exemplet ovan betyder:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   self.name = name   `

att namnet sparas i just det objekt som håller på att skapas.

Om vi skapar två objekt:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   dog1 = Dog("Buddy")dog2 = Dog("Max")   `

så får varje objekt sitt eget värde på name.

7\. \_\_str\_\_ - används när objektet ska visas som text
=========================================================

Om man skriver ut ett objekt:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   print(dog)   `

så försöker Python få fram en textrepresentation av objektet.

Om klassen innehåller \_\_str\_\_, används den:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   class Dog:    def __init__(self, name):        self.name = name    def __str__(self):        return f"Dog named {self.name}"dog = Dog("Buddy")print(dog)   `

Resultat:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Dog named Buddy   `

Om \_\_str\_\_ inte finns, visas ofta något tekniskt och mindre användbart, till exempel objektets adress i minnet.

Alltså:

*   \_\_str\_\_ används av print(objekt)
    
*   också av str(objekt)
    
*   och ofta i f-strängar
    

Det är objektets **mänskligt läsbara textform**.

8\. \_\_len\_\_ - används av len(...)
=====================================

Om man skriver:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   len(obj)   `

så försöker Python anropa:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   obj.__len__()   `

Exempel:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   class Team:    def __init__(self, members):        self.members = members    def __len__(self):        return len(self.members)team = Team(["Anna", "Bob", "Eva"])print(len(team))   `

Resultat:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   3   `

Detta betyder att objektet beter sig som något som har en storlek eller längd.

\_\_len\_\_ används alltså när objektet ska fungera som en slags container.

9\. \_\_iter\_\_ - används när objektet ska kunna itereras
==========================================================

Om man skriver:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   for x in obj:    ...   `

måste Python först kunna få en iterator från objektet.

Det görs via:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   obj.__iter__()   `

Exempel:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   class Numbers:    def __init__(self):        self.data = [1, 2, 3]    def __iter__(self):        return iter(self.data)nums = Numbers()for n in nums:    print(n)   `

Här gör \_\_iter\_\_ att objektet kan användas i en for-loop.

Det betyder att objektet är **itererbart**.

10\. \_\_next\_\_ - används för att hämta nästa värde i en iteration
====================================================================

När iterationen väl har börjat behöver Python kunna hämta nästa element, ett i taget.

Det görs med:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   __next__()   `

Ett enkelt exempel:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   class Counter:    def __init__(self):        self.current = 0    def __iter__(self):        return self    def __next__(self):        if self.current < 3:            self.current += 1            return self.current        raise StopIteration   `

Om vi skriver:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   c = Counter()for x in c:    print(x)   `

så händer ungefär detta:

1.  Python anropar c.\_\_iter\_\_()
    
2.  Python anropar sedan \_\_next\_\_() om och om igen
    
3.  när StopIteration kastas avslutas loopen
    

\_\_next\_\_ används alltså i iteratorer för att leverera nästa värde.

11\. Sambandet mellan syntax och specialmetoder
===============================================

Här blir den stora bilden tydlig.

Det som ser ut som vanlig Python-syntax är ofta kopplat till specialmetoder:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   obj = MyClass()        -> __init__print(obj)             -> __str__len(obj)               -> __len__for x in obj:          -> __iter__ och __next__   `

Alltså:

**Python-syntax -> specialmetod -> objektets beteende**

Detta är en mycket viktig idé.Den visar att klasser i Python inte bara är "en skolövning i OOP", utan ett sätt att ansluta sina egna objekt till hur språket fungerar.

12\. Hur detta leder fram till klasser
======================================

Eftersom nästan allt i Python är objekt behöver det också finnas ett sätt att definiera **nya typer av objekt**.

Det är just det en klass gör.

En klass beskriver:

*   vilka attribut ett objekt ska ha
    
*   vilka metoder objektet ska ha
    
*   vilka specialmetoder objektet ska stödja
    

Exempel:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   class Dog:    def __init__(self, name):        self.name = name    def __str__(self):        return f"Dog({self.name})"   `

Här definierar klassen en ny typ av objekt.

När vi sedan skapar ett objekt:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   dog = Dog("Buddy")   `

så får vi ett konkret exemplar, en **instans**, av klassen.

13\. Varför detta kan kännas svårt i början
===========================================

Problemet i många kursförklaringar är att man börjar direkt med:

*   klass
    
*   objekt
    
*   arv
    
*   metoder
    

utan att först visa att detta egentligen kommer ur Pythons allmänna modell.

Om man inte först förstår att:

*   värden är objekt
    
*   funktioner är objekt
    
*   språkets syntax ofta bygger på metodanrop
    
*   specialmetoder styr mycket av detta beteende
    

då känns klasser lätt som något konstigt, konstlat och byråkratiskt.

Men när man ser helheten blir klasser mer logiska.

De är bara ett sätt att säga:

**jag vill definiera en egen typ av objekt som beter sig enligt Pythons regler.**

14\. En enkel kedja att minnas
==============================

Man kan sammanfatta hela idén så här:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Python bygger på objektobjekt kan ha attribut och metoderspråkets syntax använder ofta specialmetoderklasser definierar nya typer av objekt__init__ sätter startvärden__str__ ger textrepresentation__len__ gör att len() fungerar__iter__ gör objektet itererbart__next__ levererar nästa värde i iteration   `

15\. Kort slutformulering för diskussion med lärare
===================================================

Om du vill uttrycka det mer kort och akademiskt på svenska kan du säga så här:

> I Python är klasser lättare att förstå om man först ser språkets objektmodell. Nästan allt i Python representeras som objekt, inklusive funktioner och inbyggda datatyper. Många språkkonstruktioner, som print(), len() och for, är i praktiken kopplade till objektens specialmetoder, till exempel \_\_str\_\_, \_\_len\_\_, \_\_iter\_\_ och \_\_next\_\_. Ur det perspektivet blir en klass ett sätt att definiera en ny typ av objekt som kan integreras i språkets befintliga mekanismer.

16\. Praktisk tolkning av de fem metoderna
==========================================

Till sist, mycket kort:

*   \_\_init\_\_ - körs när objektet skapas
    
*   \_\_str\_\_ - används när objektet visas som text
    
*   \_\_len\_\_ - används av len(obj)
    
*   \_\_iter\_\_ - gör att objektet kan användas i for
    
*   \_\_next\_\_ - hämtar nästa värde under iteration
