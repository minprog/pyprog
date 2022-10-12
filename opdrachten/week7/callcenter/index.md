# Call center

Computers worden veelal gebruikt voor het simuleren van situaties die in de werkelijkheid kunnen gebeuren.
Zo kan er bijvoorbeeld worden gesimuleerd hoe een regenbui effect heeft op het waterpeil, wat er gebeurt binnen de bloedstroom in een ader of hoe mensen zich bewegen in een menigte. Je hebt eerder in deze cursus ook al een kleine simulatie gebouwd.
Dit keer gebruiken we simulaties als onderwerp om te oefenen met objectgeoriënteerd programmeren.

## Opdracht

Schrijf, in een map genaamd `callcenter.py`, een programma dat de inkomende telefoongesprekken bij een callcenter simuleert. In deze map krijg je de bestanden `event.py` en `simulatie.py`.

Deze opdracht is opgesplitst in twee delen:

* Bij het eerste deel worden bellers niet in een wachtrij gezet als er geen telefonisten beschikbaar zijn, zij moeten dus op een later moment terugbellen.

* Bij het tweede deel worden bellers in deze gevallen wel in een wachtrij geplaatst. We nemen hierbij aan dat bellers niet ophangen voordat ze zijn geholpen en dus in de wachtrij blijven.

In beide gevallen is het voor de simulatie nodig om te weten:

* hoeveel werknemers er beschikbaar zijn,
* hoe lang de simulatie duurt,
* wat de gemiddelde lengte van een gesprek is,
* en wat de frequentie van inkomende telefoongesprekken is.

## Code

Je zal het misschien al geraden hebben: in deze opdracht gaan we object geörienteerd programmeren. We hebben twee classes de `Event` class en de `Simulation` class.

### Event

Bij een callcenter komen er gesprekken binnen, deze moeten worden opgenomen en later ook weer opgehangen. Naar beide gebeurtenissen refereren we als 'events'.
Deze events kunnen we in een class stoppen, waarbij elk event een gebruiker, tijdstip en type (`dial_in` of `hang_up`) heeft. Natuurlijk heeft een event, net zoals als ieder object, een eigen id.
Creeër deze class in het bestand `event.py`.

### Simulation

Daarnaast moeten we het hele process simuleren. Dit doen we met behulp van de `Simulation` class.
Deze class bestaat uit de volgende functies:

    def __init__(self, ...):
        """
        Initialise a simulation
        """

    def accept_call(self, ...):
        """
        Accept a call from a user
        """

    def add_call(self, ...):
        """
        Add an incoming call to the simulation
        """

    def run_sim(self):
        """
        Run a simulation of a callcenter
        """

### Deel 1
In de simulatie moeten evenementen (inkomende telefoongesprekken) worden gegenereerd. Deze telefoongesprekken kunnen worden opgenomen of afgewezen (wanneer er niet genoeg werknemers beschikbaar zijn).
Wanneer een gesprek wordt opgenomen, moet er een nieuw evenement worden gegenereerd: een ophang evenement.

Daarnaast geldt dat bij elk inkomend gesprek (zowel bij opnemen en afwijzen) er een nieuw `dial_in` evenement moet worden teogevoegd op basis van de belfrequentie. De belfrequentie representeert de maximale tijd tussen inkomende gesprekken.

Dit houdt dus in dat je een verzameling evenementen krijgt die op chronologische volgorde moeten worden behandeld.

Je simulatie moet stoppen wanneer:

* er geen evenementen meer zijn die moeten plaatsvinden (dit zou niet mogen gebeuren),
* de tijdlimiet is bereikt.

### Deel 2
Nu je een eerste versie van de simulatie hebt gemaakt, kan je dit gaan uitbreiden. In plaats van het simpelweg afwijzen van bellers wanneer er niet genoeg werknemers vrij zijn, gaan we nu bellers toevoegen aan een wachtrij.

Voeg hiervoor de boolean `queue` toe aan je arguementen bij je init functie in de simulatie class.
Zorg vervolgens dat de bellers in de wachtrij voorrang hebben op nieuwe bellers op het moment dat er een werknemer vrij komt.

## Tips

**Deel 1**

* Vergeet niet dat je argumenten kan toevoegen aan je simulatie, denk bijvoorbeeld aan een lijst van events of een waarde die bijhoudt hoeveel werknemers er wel/niet in gesprek zijn.
* De duratie van een telefoongesprek kan bepaald worden op basis van de Poisson verdeling (`np.random.poisson(self.avg_length)`).

**Deel 2**

* Zodra een beller uit de wachtrij komt, begint het gesprek. Zorg ervoor dat je de tijd van het events update naar de tijd van het gesprek (in plaats van het tijd van binnenkomen in de wachtrij).


## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder. Let op: we werken in deze simulatie met willekeurige getallen, dus elke keer als je je programma runt, zal dit een andere output hebben.

### Deel 1

    Een simulatie van 20 minuten is gestart met 2 werknemers, gemiddelde gespreksduur van 5 minuten en een belfrequentie van 7
    Gebruiker 0 krijgt op tijd 0 iemand aan de lijn voor 5 minuten.
    Gebruiker 0 hangt op op tijd 5.
    Gebruiker 1 krijgt op tijd 6 iemand aan de lijn voor 4 minuten.
    Gebruiker 1 hangt op op tijd 10.
    Gebruiker 2 krijgt op tijd 12 iemand aan de lijn voor 6 minuten.
    Gebruiker 3 krijgt op tijd 15 iemand aan de lijn voor 6 minuten.
    Gebruiker 4 krijgt op tijd 15 'in gesprek' toon.
    Gebruiker 2 hangt op op tijd 18.
    Gebruiker 5 krijgt op tijd 19 iemand aan de lijn voor 9 minuten.

    Een simulatie van 20 minuten is gestart met 4 werknemers, gemiddelde gespreksduur van 8 minuten en een belfrequentie van 4
    Gebruiker 0 krijgt op tijd 0 iemand aan de lijn voor 4 minuten.
    Gebruiker 1 krijgt op tijd 1 iemand aan de lijn voor 10 minuten.
    Gebruiker 2 krijgt op tijd 2 iemand aan de lijn voor 4 minuten.
    Gebruiker 0 hangt op op tijd 4.
    Gebruiker 2 hangt op op tijd 6.
    Gebruiker 3 krijgt op tijd 6 iemand aan de lijn voor 5 minuten.
    Gebruiker 4 krijgt op tijd 6 iemand aan de lijn voor 10 minuten.
    Gebruiker 5 krijgt op tijd 8 iemand aan de lijn voor 8 minuten.
    Gebruiker 6 krijgt op tijd 10 'in gesprek' toon.
    Gebruiker 1 hangt op op tijd 11.
    Gebruiker 3 hangt op op tijd 11.
    Gebruiker 7 krijgt op tijd 13 iemand aan de lijn voor 10 minuten.
    Gebruiker 8 krijgt op tijd 15 iemand aan de lijn voor 12 minuten.
    Gebruiker 4 hangt op op tijd 16.
    Gebruiker 5 hangt op op tijd 16.
    Gebruiker 9 krijgt op tijd 19 iemand aan de lijn voor 10 minuten.

### Deel 2

    Een simulatie van 20 minuten is gestart met 4 werknemers, gemiddelde gespreksduur van 8 minuten en een belfrequentie van 4
    Gebruiker 0 krijgt op tijd 0 iemand aan de lijn voor 9 minuten.
    Gebruiker 1 krijgt op tijd 3 iemand aan de lijn voor 9 minuten.
    Gebruiker 2 krijgt op tijd 6 iemand aan de lijn voor 9 minuten.
    Gebruiker 3 krijgt op tijd 8 iemand aan de lijn voor 14 minuten.
    Gebruiker 0 hangt op op tijd 9.
    Gebruiker 4 krijgt op tijd 11 iemand aan de lijn voor 6 minuten.
    Gebruiker 1 hangt op op tijd 12.
    Gebruiker 5 krijgt op tijd 12 iemand aan de lijn voor 5 minuten.
    Gebruiker 6 wordt toegevoegd aan de wachtrij.
    Gebruiker 7 wordt toegevoegd aan de wachtrij.
    Gebruiker 8 wordt toegevoegd aan de wachtrij.
    Gebruiker 2 hangt op op tijd 15.
    Gebruiker 6 krijgt op tijd 15 iemand aan de lijn voor 5 minuten.
    Gebruiker 9 wordt toegevoegd aan de wachtrij.
    Gebruiker 4 hangt op op tijd 17.
    Gebruiker 7 krijgt op tijd 17 iemand aan de lijn voor 8 minuten.
    Gebruiker 5 hangt op op tijd 17.
    Gebruiker 8 krijgt op tijd 17 iemand aan de lijn voor 5 minuten.
    Gebruiker 10 wordt toegevoegd aan de wachtrij.
    Gebruiker 6 hangt op op tijd 20.
    Gebruiker 9 krijgt op tijd 20 iemand aan de lijn voor 4 minuten.
