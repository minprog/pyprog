# Memory Model

Python maakt onderscheid tussen 'mutable' en 'immutable' types. Een
waarde van een immutable type kan niet worden aangepast zonder dat er
een kopie van gemaakt wordt. Een waarde van een mutable type kan wel
worden aangepast zonder een kopie te maken.

Elk type is mutable of immutable. 

immutable types: `bool`, `int`, `float`, `str`, `tuple`, enkele andere types

mutable types: `list`, `set`, `dictionary`, alle andere types


## int (immutable type)

In dit voorbeeldprogrammma verwijzen variabelen `a` en `b` naar een
waarde van het type `int` welke immutable is.

    a = 1
    b = a
    a += 100
    print("a:", a, "b:", b)

Als we dit programma uitvoeren in
[PythonTutor](https://pythontutor.com/) met de optie "render all
objects on the heap" zien we wat er gebeurt. Na uitvoeren van de
eerste regel verwijst variable `a` naar waarde `1`.

![](mm_int2.png){: style="width:20rem;"}

Na de volgende regel verwijst variable `b` naar dezelfde waarde:

![](mm_int3.png){: style="width:20rem;"}

Dan wordt de waarde waar `a` naar wijst aangepast (`+= 100`), en omdat
`a` naar een 'immutable' type verwijst wordt eerst een kopie van deze
waarde gemaakt zodat de waarde waar `b` naar verwijst, niet wordt
aangepast:

![](mm_int4.png){: style="width:20rem;"}

Als we `a` en `b` vervolgens printen zien we dat ze inderdaad twee
verschillende waarden hebben.

![](mm_int5.png){: style="width:20rem;"}


## str (immutable type)

In dit voorbeeldprogramma verwijzen `a` en `b` naar een waarde van het type `str`. 

    a = "hello"
    b = a
    a += " world"
    print(f"a: '{a}' b: '{b}'")
    
Omdat een `str` net als een `int` 'immutable' is, gebeurt hier
hetzelfde en zien we na het printen dat `a` en `b` twee
verschillende waarden hebben.

![](mm_str5.png){: style="width:20rem;"}

Geen verassingen tot nu toe.


## list (mutable type)

Maar in dit voorbeeldprogramma verwijzen `a` en `b` naar een waarde
van het type `list` wat een `mutable` type is. Het resultaat is nu
anders.

    a = [1, 2, 3]
    b = a
    a += [100]
    print(f"a: '{a}' b: '{b}'")

Na uitvoeren van de eerste regel verwijst variable `a` naar een lijst
`[1, 2, 3]`.

![](mm_list2.png){: style="width:20rem;"}

Na de volgende regel verwijst variable `b` naar dezelfde waarde:

![](mm_list3.png){: style="width:20rem;"}

Dan wordt de waarde waar `a` naar wijst aangepast (`+= [100]`), en
omdat `a` naar een 'mutable' type verwijst wordt **geen** kopie van
deze waarde gemaakt en dus wordt de waarde waar `b` naar verwijst ook
aangepast.

![](mm_list4.png){: style="width:20rem;"}

Bij het printen zien we dan ook dat voor variable `a` en `b` dezelfde
waarde hebben wat in de eerdere voorbeeldprogramma's met 'immutable'
types niet het geval was.

![](mm_list5.png){: style="width:20rem;"}


## Motivatie

Een rede waarom er geen kopie van een 'mutable' type wordt gemaakt
vooraf aan een aanpassing, is om te voorkomen dat bijvoorbeeld een
grote lijst bij elke kleine aanpassing eerst helemaal gekopieerd moet
worden, want dat zou een programma heel traag maken.


## Functie aanroep

Dit verschil tussen 'mutable' en 'immutable' types zorgt ook
voor een verschil bij het aanroepen van functies. In het onderstaande
voorbeeldprogramma roepen we functie `add_100()` aan met een waarde van
een 'immutable' en 'mutable' type.

    def add_100(immu: int, mu: list) -> None:
        immu +=  100
        mu   += [100]
        print("2) immu:", immu, "mu:", mu)
    
    immutable =  1
    mutable   = [1, 2, 3]
    print("1) immutable:", immutable, "mutable:", mutable)
    add_100(immutable, mutable)
    print("3) immutable:", immutable, "mutable:", mutable)

Vooraf aan de functie worden de waarden geprint als:

    1) immutable: 1 mutable: [1, 2, 3]
    
In de functie worden beide waarden aangepast (`100`
toegevoegd) en geprint als:

    2) immu: 101 mu: [1, 2, 3, 100]

Maar omdat in de functie vooraf aan de aanpassing van de waarde van
het 'immutable' type een kopie wordt gemaakt, wordt de originele
waarde buiten de functie niet veranderd. In de print na de functie is
dan ook alleen de waarde van het 'mutable' type aangepast:

    3) immutable: 1 mutable: [1, 2, 3, 100]

## Voorkom bugs

Om bugs te voorkomen is het dus belangrijk om tijdens het programmeren
te weten of je een waarde van een 'mutable' of 'immutable' type
aanpast. Bij 'mutable' types wil je altijd in je hoofd de verwijzingen
voor je zien als pijltjes zoals het wordt weergegeven in
PythonTutor. Bij 'immutable' types is dat niet nodig, omdat toch
altijd eerst een kopie wordt gemaakt vooraf aan elke aanpassing zodat
het niet tot bugs leiden.

Het is goed om de 'immutable' uit je hoofd te leren, alle andere
types zijn dan 'mutable'.

immutable types: `bool`, `int`, `float`, `str`, `tuple`, enkele andere types

De 'enkele andere types' laten we achterwegen, want die komen niet voor
in dit vak.
