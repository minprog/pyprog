# Installatie

Voor deze cursus heb je **Python** nodig en een **editor**. Hieronder staan verschillende opties om de benodigdheden te installeren. Heb je problemen met de installatie, check dan eerst bij de assistenten en je docent, en als dat niet helpt, neem dan **direct** contact op via <pyprog@proglab.nl>. Een mislukte installatie is namelijk géén reden voor een uitzondering op de deadlines!

## Python

-   Als je Ubuntu gebruikt, dan heb je mogelijk al Python. Check dit door in een terminal het commando `python3 -V` te geven. Waarschijnlijk heb je dan Python 3.10. Installeer anders de best beschikbare versie via:

        sudo apt-get update
        sudo apt-get install python3 python3-pip

    **Had je al eerder deze pagina gebruikt?** Let op dat `python3-pip` hierboven is toegevoegd. Je kunt het gewoon nog een keer installeren.

-   Als je met macOS werkt, dan heb je misschien al Python. Check dit door in een terminal het commando `python3 -V` te geven. Misschien heb je Python 3.8 of eerder. In dat geval is het aan te raden een nieuwe versie te installeren, en liefst Python 3.11.

    Als je gaat installeren, doe dit dan door op de Python-homepage een Python installer te downloaden en uit te voeren: <https://www.python.org/downloads/>. Hiermee heb je meteen de nieuwste versie.

-   Als je met Windows werkt, dan heb je misschien al Python. Check dit door in de command prompt (`cmd.exe`) het commando `python -V` te geven. Misschien heb je Python 3.8 of eerder. In dat geval is het aan te raden een nieuwe versie te installeren, en liefst Python 3.11.

    Als je gaat installeren, doe dit dan door op de Python-homepage een Python installer te downloaden en uit te voeren: <https://www.python.org/downloads/>. Hiermee heb je meteen de nieuwste versie. **Kies "Add python to PATH" tijdens de installatie. Mogelijk moet je hiervoor een "Advanced" install doen.**

## Een simpele editor

Voor beginnende programmeurs is het **niet** aan te raden om te werken met Visual Studio Code. Dat komt omdat VSCode veel automatische tools installeert om jou het leven "makkelijk" te maken. Maar als je niet begrijpt wat er gebeurt, dan helpt het niet. Ook kan het je hinderen in het leren programmeren.

Laat je dus vooral niet verleiden door iemand die het wel even voor je instelt, en gebruik tools die je goed begrijpt, zodat je je lekker kan richten op waar het om gaat :-)

Daarom is de beste aanrader voor beginners om een goede, maar simpele editor te gebruiken. Voor elk besturingssysteem zijn er diverse opties, maar we geven er hier ééntje.

-   Als je Ubuntu gebruikt, dan is Notepadqq een goede optie. Installeer deze via:

        sudo apt-get update
        sudo apt-get install notepadqq

-   Als je macOS gebruikt, dan is Textmate een goede optie. Installeer deze via de website <https://macromates.com>.

    -   Heb je je programmeer-directory geopend in Textmate? Druk dan op ctrl-shift-O om een terminal te openen. Dan sta je direct op de juiste plek om je programma te runnen met `python3 programma.py`.

-   Als je Windows gebruikt, dan is Notepad++ een goede optie. Installeer deze via de website <https://notepad-plus-plus.org>.

Maak in alle gevallen een speciale directory om aan je Python-opdrachten te werken, liefst een directory die automatisch wordt gebackupt (Dropbox, Surfdrive, Onedrive, enz.). 

## Visual Studio Code

Heb je al programmeerervaring en weet je hoe je je eigen computer goed installeert en netjes houdt, dan is Visual Studio Code zeker een optie. Zorg ervoor dat VSCode niet zomaar allerlei plugins installeert die bijvoorbeeld `import`s toevoegen aan jouw code.

Volg dan de stappen van [deze pagina](https://code.visualstudio.com/docs/python/python-tutorial) om VS Code goed in te stellen. Volg de stappen t/m Configure and Run the Debugger, en als het goed is kun je het installeren van Python overslaan omdat je dat hierboven al hebt gedaan!
