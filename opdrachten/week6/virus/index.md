# Simuleren met virussen

![](virus.jpg)

Voor beleidsmakers en de farmaceutische industrie is het belangrijk om de succeskans van een geneesmiddel te bepalen. Omdat vele factoren een rol spelen is het lastig om deze kans in een wiskunde formule te vatten, en daarom biedt het doen van simulaties een uitkomst. In deze opdracht ga je virusdeeltjes simuleren die kunnen reproduceren en sterven. We bouwen deze opdracht stap voor stap op tot een complete, maar versimpelde simulatie.

Bij deze opdracht focussen we niet alleen op het idee van simuleren, maar je gaat ook zorgvuldiger dan voorheen je code testen. Bij elke tussenstap vind je een codeblok met een functie die jij gaat implementeren. In de uitleg staat altijd een kopje "Controle", met aanwijzingen over hoe jij kan checken of je functie voldoet aan de verwachtingen. Deze aanwijzingen zijn niet compleet! Het kan zijn dat je tegen problemen aanloopt die hierdoor niet gecheckt worden. Je moet dus ook oefenen met het zelf nadenken over poteniële problemen. Het doel van tussentijdse checks is om te voorkomen dat fouten zich opstapelen. Als een fout zich pas op het allerlaatst vertoont, is het namelijk veel lastiger om de ware oorzaak te vinden.

Tot slot spelen "list comprehensions" bij deze opdracht een grote rol. Om extra motivatie te geven deze te gebruiken, staat bij voor opdrachten een limiet voor het aantal regels code dat gebruikt mag worden voor de oplossing. Lukt dat niet goed? Maak je oplossing dan (zo mogelijk) eerst werkend zonder list comprehensions en vraag hulp aan de assistenten met het omzetten naar list comprehensions.

## Stap 1: Virusgenoom

DNA is een streng van moleculen die nucleotiden worden genoemd. Elk DNA-molecuul bestaat in feite uit twee strengen van dergelijke nucleotiden, die bovendien bij elke nucleotide met elkaar verbonden zijn. De verbonden nucleotiden noemen we basenparen. Omdat deze paren altijd in vaste combinaties voorkomen kunnen we bij het typeren van een dubbele DNA-streng volstaan met het specificeren van de namen van de nucleotiden van één streng. De namen zijn: adenine (A), cytosine (C), guanine (G) en thymine (T). Bij elke menselijke cel bestaat de DNA-streng uit miljarden van zulke basenparen. Ook veel virussen zijn opgebouwd uit precies dezelfde typen cellen.

(Disclaimer: wij zijn geen biologen en coronavirussen zijn RNA-virussen en geen DNA-virussen :-))

* Voeg deze regels toe bovenaan een bestand `virus.py`:

        import random
        import string

* Schrijf een functie `generateVirus(length)`.
    
    * Deze functie accepteert één argument, `length`, dat is een integer die de lengte van het virusgenoom representeerd.
    * De functie moet een string returnen bestaande uit een willekeurige sequentie van nucleotides.

* Oh, one more thing: Je mag maar **twee regels code** gebruiken voor deze functie (dat is inclusief de regel `def generateVirus(length):`).

    * Gebruik een list comprehension en de `"".join()` methode van een string.

    * Kijk eens naar de `random.choice()` functie.

### Testen

Maak en print virussen van verschillende lengtes om te kijken of deze kloppen. De uitkomst is natuurlijk willekeurig, dus kijk goed of de genomen inderdaad verschillen, en dat je over een paar keer draaien alle nucleotiden weleens voorbij ziet komen.

len(generateVirus(3)) == 3
type(generateVirus(0)) == str


Er zijn diverse manieren om te testen:

* Je kunt gewoon `generateVirus()` een paar keer aanroepen in de cel hieronder en de output bestuderen.

* Je kunt een loop schrijven die `generateVirus()` aanroept en de verschillen tussen de verschillende virussen bestuderen.

* Als je een "eigenschap" weet te formuleren van de uitkomst van `generateVirus()` dan kun je ook een `assert` schrijven. Deze checkt of iets werkt zoals verwacht. Hieronder staan al twee asserts waaraan je functie moet voldoen. Als er geen foutmelding verschijnt, dan is de assert "akkoord".

* Combinaties van alle bovenstaande.


## Stap 2: Muteren

Zodra een virus wordt geboren heeft deze een kans te muteren.
Muteren is het veranderen van één willekeurig nucleotide voor een willekeurige ander.
Bijvoorbeeld van AGTC naar ATTC.

* Schrijf een functie `mutate(virus)`.
	* Deze functie accepteert één argument, `virus`, dat is een string van nucleotides.
	* De functie moet een string returnen bestaande uit dezelfde nucleotides, waarvan er één is gemuteerd.
* Geen regellimiet dit keer, maar als je jezelf wilt uitdagen: 3 (of minder) regels is mogelijk.
* Een mutatie waarna het resultaat hetzelfde is, telt niet als mutatie.

### Tips

* Kijk eens naar de `random.randrange()` functie!
* Gebruik list slicing.

### Controle

* Controleer of de mutate functie altijd het virus veranderd. Je zou bijvoorbeeld een groot aantal (1000) virussen kunnen aanmaken en deze kunnen muteren. Is ieder virus anders na mutatie?"
* Controleer of de lengte van het virus gelijk is gebleven na mutatie.

## Stap 3: Afsterven

De afgelopen twee tussenstappen hebben we met losse virussen gewerkt. Die hebben we weergegeven als een string. Voor onze toekomstige simulatie willen we alleen werken met een grote hoeveelheid virussen. Om zo'n populatie weer te geven, kunnen we een lijst maken van al die virussen. Dat zou er als volgt uit kunnen zien:

 ```['"ACTG", "AGAA", "ACCG", "GTCA"]``` 


Met deze structuur gaan we nu verder werken. Want virussen kunnen natuurlijk sterven. Ze sterven niet allemaal tegelijk, maar elke tijdstap heeft elke virus een kans om te sterven. Met de volgende functie gaan we het resultaat van één zo'n tijdstap weergeven.

* Schrijf een functie `kill(viruses, mortalityProb)`.
	* Deze functie accepteert twee argumenten:
		* `viruses` is een lijst van virusgenomen.
		* `mortalityProb` is een float tussen 0 en 1 (inclusief) die de kans op het afsterven per virusdeeltje representeert.
	* De functie moet een **nieuwe** lijst returnen met daarin de virusgenomen die het hebben overleefd.
* Let op, elk virusgenoom heeft een individuele kans om af te sterven. Dus bij een `mortalityProb` van 0.2 overleeft gemiddeld 80% van de viruspopulatie het, maar dit kan fluctueren!
* Je mag hier **twee regels code** gebruiken (dat is inclusief de regel `def kill(viruses, mortalityProb):`).

### Tip

* Gebruik een list comprehension!


### Controle

* Bedenk hoeveel virussen er gemiddeld over zouden moeten blijven na deze functie. Let op dat er veel willekeur in deze functie is, dus dat het niet gek is als het een klein beetje erboven of eronder zit.
* Test je functie niet alleen met waarden in het midden, maar ga ook op zoek naar de uiterste. Klopt er wat er gebeurt als ik de sterftekans op 0 of 1 zet?


## Stap 4: Reproductie

Een virus heeft een kans zich voort te planten op elke tijdstap in de simulatie.
Als een virus zich voortplant dan heeft het kind exact dezelfde DNA string als de ouder.
Behalve als het kind muteert, dan is er één basepaar anders.

* Schrijf voor reproductie een functie `reproduce(viruses, mutationProb, reproductionProb)`.
	* Deze functie accepteert drie argumenten:
		* `viruses` is een lijst van virusgenomen.
		* `mutationProb` is een float tussen 0 en 1 (inclusief) die de kans op mutatie bij het kind virusdeeltje representeert.
		* `reproductionProb` is een float tussen 0 en 1 (inclusief) die de kans op reproductie per virusdeeltje representeert.
* De functìe moet de lijst van de totale populatie van virusgenomen returnen. Dat is dus inclusief de ouders!
* Let op, elk virusgenoom heeft een individuele kans om te reproduceren. Dus bij een `reproductionProb` van 0.2 reproduceert gemiddeld 20% van de populatie, maar dit kan fluctueren!
* Geen regellimiet dit keer, maar als je jezelf wilt uitdagen: 2 regels is mogelijk.

### Controle

* Controleer net als bij vorige functie of deze functie ongeveer het verwachte aantal virussen teruggeeft.
* Controleer of er ook daadwerkelijk virussen gemuteerd zijn.


## Stap 5: Resistentie

![](medicine.png)

Voor dat we kunnen gaan simuleren, voegen we een geneesmiddel toe aan onze simulatie.
Virussen kunnen resistent zijn tegen zo'n geneesmiddel; bij de reproductie kan een mutatie ervoor zorgen dat de resistentie ontstaat. Een resistent virus is een virus dat `AAA` in de DNA-streng heeft.
Zodra het geneesmiddel wordt geintroduceerd, kunnen alle virussen behalve resistente virussen niet meer reproduceren.

* Schrijf een functie `isResistent(virus)`.
	* Deze functie accepteert één argument, `virus`, dit is een virusgenoom.
	* De functie moet een boolean returnen welke aangeeft of het virus resistent is (`True`) of niet (`False`).
* Een virus is enkel resistent als `AAA` achterelkaar voorkomt.

### Tip

* Kijk eens naar de functie `string.find()`!

### Controle
* Test deze functie op verschillende virussen om te kijken of het de resistente virussen herkent.

## Reproductiekans als functie van de populatiegrootte

Naarmate er meer virusdeeltjes aanwezig zijn, wordt de kans op reproductie kleiner.
Er is simpelweg niet genoeg ruimte voor alle virusdeeltjes.
Er is een negatief linear verband tussen het aantal virussen en de reproductie kans.
De kans op reproductie is gelijk aan `(1 - (grootte_van_virus_populatie / maximaal_aantal_virussen)) * maximale_reproductie_kans`.
De functie om de kans per individueel virusdeeltje in een populatie te berekenen vind je hieronder:


    def reproductionProbability(viruses, maxReproductionProb, maxPopulation):
        return (1 - (len(viruses) / maxPopulation)) * maxReproductionProb if maxPopulation > 0 else 0



## Stap 6: Simuleren met een geneesmiddel

Nu we een representatie hebben voor virussen, deze kunnen laten muteren, doen sterven, laten reproduceren en resistent kunnen laten zijn, kunnen we gaan simuleren.

De simulatie werkt als volgt. Tijdens elke tijdstap:
* Laten we eerst virussen afsterven,
* Daarna berekenen we de productiekans,
* Daarna laten we ze reproduceren

**Maar** vanaf de 100e tijdstap voegen we een geneesmiddel toe aan de simulatie, en kunnen enkel resistente virussen reproduceren.



Dus:
* Schrijf een functie genaamd `simulate(viruses, mortalityProb, mutationProb, maxReproductionProb, maxPopulation, timesteps = 500)`.
	* Deze functie accepteert vijf argumenten, en één optioneel argument:
		* `viruses` is een lijst van virusgenomen.
		* `mortalityProb` is een float tussen 0 en 1 (inclusief) die de kans op het afsterven per virusdeeltje representeert.
		* `maxReproductionProb` is een float tussen 0 en 1 (inclusief) die de maximale kans op reproductie per virusdeeltje representeert.
		* `maxPopulation` is een integer voor de maximale populatiegrootte.
		* `mutationProb` is een float tussen 0 en 1 (inclusief) die de kans op mutatie bij reproductie representeert.
		* `timesteps` is een integer en een optioneel argument die het aantal tijdstappen in de simulatie aangeeft.
	* De functie moet een lijst returnen met daarin de populatiegrootte (een integer) op elke tijdstap.

### Pseudocode
Hieronder vind je de pseudocode voor de simulate functie. Kijk er goed naar, want de volgorde van de verschillende stappen in de simulatie is belangrijk. Zo kunnen er andere resultaten uitkomen als de virussen bijvoorbeeld eerst reproduceren en dan pas afsterven. 
Denk van te voren goed na over wat de stappen "reproduce with medicine" and "reproduce without medicine" precies inhouden. Wat het verschil is tussen de twee en hoe je dit kan implementeren

    1  function simulate
    2     let population_sizes be a list
    3     for every timestep t
    4         kill viruses
    5         calculate reproduction probability
    6         if timstep t >= 100
    7             reproduce with medicine
    8         else
    9             reproduce without medicine
    10        add size of population to population_sizes
    11    return population_sizes


### Tips
Voor deze opdracht is het wellicht wat lastiger om zelf tests te bedenken. Daarom hebben we er onder de functie al twee meegegeven. De eerste controleert of het resultaat inderdaad bestaat uit 501 lijsten (500 tijdstappen plus de beginsituatie). De tweede controleert of, gegeven die variabelen, de simulatie de juiste resultaten geeft.


    def simulate(viruses, mortalityProb, mutationProb, maxReproductionProb, maxPopulation, timesteps = 500):


### Testen

    # test 1
    viruses = [generateVirus(4) for _ in range(100)]
    assert 501 == len(simulate(viruses, 1, 0, 0, 0))

    # test 2
    sims = []
    n = 100
    for i in range(n):
        viruses = [generateVirus(4) for _ in range(100)]
        sims.append(simulate(viruses, 0.1, 0.1, 0.5, 100, timesteps = 1000)[-1])
    average = sum(sims) / n

    # note: this might fluctuate a little, so if needed you can enlarge the range of valid outcomes
    assert 25 < average < 30

## Afronding: grafieken

Hieronder vind je code voor het maken van grafieken op basis van jouw zelfgeschreven functies. Je hoeft niks aan te passen aan de onderstaande code. Dit is natuurlijk de ultieme test: het zal alleen werken als alle bovenstaande functies precies volgens de specificatie geïmplementeerd zijn.

Kijk eens door de code of je snapt wat er gebeurt. De functies van de `matplotlib`-library zijn eenvoudig, maar de meeste hebben een erg cryptische naam. Eventueel kun je in de documentatie van matplotlib kijken wat de functie doet. En als je geïnteresseerd bent en nog tijd hebt, probeer dan zelf nog onderaan een interessante grafiek toe te voegen!

    import matplotlib.pyplot as plt


### Grafiek van één simulatie

Hieronder een grafiek van één simulatie van jouw functie! :)

    # uitkomst van de simulatie
    simulate_result = simulate(viruses, 0.1, 0.1, 0.5, 100, timesteps = 500)

    fig = plt.figure(figsize=(15, 10))
    ax = plt.axes()

    # plotten van de data
    ax.plot(range(501), simulate_result)

    # opmaak van de grafiek
    plt.title('Simulation')
    plt.xlabel('Timestep')
    plt.ylabel('Number of viruses')
    plt.ylim(0,110)
    plt.xlim(0,500)

    plt.show()


### Grafiek van meerdere simulaties

Zoals je misschien opviel bij de bovenstaande grafiek, het resultaat wisselt nogal. In onderstaande kun je zien dat er hoofdzakelijk twee manieren zijn waarop het kan verlopen.

    fig = plt.figure(figsize=(15, 10))
    ax = plt.axes()

    # uitvoeren van twintig simulaties
    for i in range(20):
        simulate_result = simulate(viruses, 0.1, 0.1, 0.5, 100, timesteps = 500)
    
        # voeg het resultaat van een simulatie toe als lijn
        ax.plot(range(501), simulate_result)

    # opmaak van de grafiek
    plt.title('Simulations')
    plt.xlabel('Timestep')
    plt.ylabel('Number of viruses')
    plt.ylim(0,110)
    plt.xlim(0,500)

    plt.show()

### Genezen/ongenezen

Als laatste grafiek gaan we kijken in hoeveel gevallen het geneesmiddel succesvol is geweest.

    cured = 0 # aantal genezen simulaties
    n_simulations = 100

    # voer de simulatie honderd keer uit, en hou bij hoeveel daarvan genezen zijn
    for i in range(n_simulations):
        simulate_result = simulate(viruses, 0.1, 0.1, 0.5, 100, timesteps = 500)
        # als de laatste tijdstap geen virussen bevat, is de persoon genezen
        if simulate_result[-1] == 0:
            cured += 1
        
    labels = 'Cured', 'Not Cured'
    sizes = [cured, n_simulations - cured]

    # maken van de pie chart
    fig1, ax1 = plt.subplots(figsize=(8, 8))
    ax1.pie(sizes, labels=labels, autopct='%1i%%',startangle=90)
    ax1.axis('equal')
    plt.title('Pie chart of cured and non cured simulations')
    plt.show()
