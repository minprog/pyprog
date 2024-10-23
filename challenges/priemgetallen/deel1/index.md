# Priemgetallen

> **Studeertip.** De challenges zijn alleen voor studenten die het vrij makkelijk vinden tot nu toe. Specifiek deze week heb je loops nodig, die eigenlijk nog niet tot de stof horen. Je kunt wel alvast kijken in je boek, de rest van hoofdstuk 4. Als je een challenge hebt gemaakt, klop dan bij het laptopcollege bij je docent aan om 'm door te spreken.

Implementeer een programma dat op verzoek het $$N$$-de priemgetal genereert.

    Naar het hoeveelste priemgetal bent u op zoek? 1000
    7919

## Achtergrond

Een computer is geweldig in het snel uitvoeren van een heleboel "domme" stappen. Een voorbeeld waar een computer zóveel effectiever is dan een enkele persoon, is het uitrekenen van priemgetallen. De definitie van een priemgetal is niet al te ingewikkeld. Maar bepalen hoeveel delers een willekeurig getal heeft kan ontzettend veel tijd kosten. Python to the rescue!

## Specificatie

- Vraag de gebruiker om de *rangorde* van het priemgetal (het hoeveelste) in te voeren. Dit moet dus een geheel en positief getal zijn.

- Als de gebruiker een rangorde invult die niet toegestaan is, dan vraag je de gebruiker opnieuw naar de rangorde. En herhalen tot de gebruiker een geldige rangorde invult. Omdat je niet weet hoe vaak dat zal zijn, moet het een `while`-loop worden.

- Ofschoon je moet controleren of het om een positief getal gaat, mag je er wel vanuit gaan dat een geheel getal wordt ingevoerd (en geen kommagetal). Dat hoef je dus niet te controleren.

- Zodra de rangorde bekend is, bereken het juiste priemgetal en rapporteer dit terug aan de gebruiker.

- Zorg dat het programma niets anders uitvoert dan dit getal, zoals in het voorbeeld bovenaan de opdracht!

- Het programma moet drie functies met de gegeven namen bevatten die alle stappen zoals onder beschreven uitvoeren.

## Probleemanalyse

Neem vóór je gaat programmeren eerst een paar minuten om met **pen en papier** te schetsen hoe je zelf het probleem aan zou pakken, hoe je het probleem kunt opdelen in overzichtelijke stappen. De specificatie hierboven geeft al wat hints daarvoor.

Bij deze opdracht nemen we je aan de hand door een aantal stappen te geven om te doorlopen tijdens het ontwikkelen van de juiste oplossing.

## Stap 1: priem-check

Een belangrijk deel van de omschrijving hierboven is dat het om priemgetallen gaat. Wat is een priemgetal? Dat moeten we in Python zien uit te drukken.

Definieer dus eerst een functie `is_priem()` met één argument die van een bepaald getal, het argument, onderzoekt of het een priemgetal is of niet. De functie moet een `bool` returnen.

Begin zo simpel mogelijk. Gebruik een `for`-loop en `%` (modulo) om te bepalen hoeveel getallen een deler zijn van het argument. Als je dit bijhoudt in de loop (tellen!), kun je na afloop van de loop bepalen of het getal een priemgetal is of niet.

## Stap 2: check een hele partij getallen

We gaan een stap verder. We kunnen de code nu hergebruiken (dus de functie aanroepen) en voor *elk* getal onder de 100 bepalen of het een priemgetal is of niet.

Definieer een functie `print_priemen_tot()` met één argument, `N`. Maak in deze functie een `for`-loop om alle getallen onder de `N` langs te loopen en bepaal voor elk van deze "kandidaat-priemgetallen" of het wel of niet een priemgetal is door de functie `is_priem` aan te roepen.

Schrijf deze procedure en maak deze goed werkend. De functie moet niets returnen, maar moet wel ieder gevonden priemgetal printen.

Klopt je antwoord? Check op internet of de geprinte getallen overeenkomen!

## Stap 3: het zoveelste priemgetal

We gaan nu terug naar het eerder beschreven doel: op zoek naar het $$N$$-de priemgetal. We geven een voorzetje voor de strategie van het programma:

- Nu zoeken we het `N`-de priemgetal; we willen niet weten of `N` een priemgetal is (zie je het verschil met stap 2?) Je kunt dus niet meer met een `for`-loop simpelweg tot `N` loopen. Immers, bij een `for`-loop weet je van tevoren hoe vaak er geïtereerd wordt en dat weten we nu niet. Je moet dus in je programma gaan bijhouden *hoeveel* priemgetallen je al gevonden hebt. Gebruik hiervoor een variabele, net als bij het bijhouden van de hoeveelheid delers in Stap 1. Merk op dat dit bijhouden van informatie in een variabele (bv. een 'teller') nu al een paar keer handig blijkt. We zullen dit meerdere keren terug zien komen bij de rest van het vak, dus oefen er goed mee!

- Definieer een functie `zoveelste_priem()`, met één argument: `N`. De functie moet vervolgens het `N`de priemgetal returnen.

- Zoals bovenaan beschreven moet bij het runnen van je programma de gebruiker om input worden gevraagd tot een geheel getal wordt gegeven. Doe dit opvragen buiten de functie en geef de input als argument aan je functie.

- Begin klein. Zorg dat je programma eerst de priemgetallen tot 10 kan vinden. Dat is klein genoeg om te zien of het programma precies doet wat de bedoeling is, en kun al snel ontdekken wat er mis gaat.

- Problemen? Print bij elke kandidaat-priem wat informatie, zodat je weet waar je bent in de berekening en je ziet of de computer ook echt jouw bedoelde strategie volgt.

## Stap 4: werkt het echt?

Loop nu de specificatie bovenaan de opdracht goed door en zorg dat je programma precies zo werkt als daar beschreven is.

## Stap 5: kleine optimalisaties

Deze stap is volledig optioneel, dus hoeft niet ingeleverd te worden. Wel goed om over na te denken en te proberen als je tijd over hebt.

We zijn hierboven zo simpel mogelijk begonnen, zodat we snel tot een *correct* programma zijn gekomen (gecontroleerd door `checkpy`). Maar met behulp van wat wiskundig inzicht kunnen we kleine optimalisaties doen, waardoor het programma sneller wordt. 

- Behalve 2 zijn *even* getallen nooit een priemgetal (dit vraagt slechts een hele kleine aanpassing van je code).

- Als je een deler vindt hoef je niet verder te zoeken omdat je dan gelijk weet dat het geen priemgetal is.

## Hints

Je kunt dit programma schrijven met alleen de Python-onderdelen die je tot nu toe hebt geleerd + loops!
