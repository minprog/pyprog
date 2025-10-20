# Installatie

Voor deze cursus heb je **Python** nodig en een **editor**.

> **ChatGPT Python kickstarter**
>
> Ga naar onze installatiehulp om stap-voor-stap begeleiding te krijgen. Hiermee installeer je Python en `mypy`. Je gaat ook een Python-programmaatje schrijven en proberen te runnen.
>
> <https://chatgpt.com/g/g-muT6gPRxL-python-kickstarter>


## Problemen?

Heb je problemen met de installatie:

1. check eerst bij de assistenten of je docent
2. ga naar de laptophelpdesk: dinsdag en donderdag 12:00--13:00 in B1.27
    - de eerste drie weken van het studiejaar kun je maandag t/m vrijdag terecht van 10.00 tot 16.00 uur in B1.19A (glazen hok)
3. als niks helpt, neem dan **direct** contact op via <mailto:pyprog@proglab.nl>

Een mislukte installatie is géén reden voor een uitzondering op deadlines!

## Python

<!-- 
    Let op: studenten hebben bij KI in principe een dual-boot laptop en 
    worden geacht Linux te gebruiken. We kiezen ervoor de deadsnakes repo
    toe te voegen en niet `uv` of iets anders te gebruiken.
-->

-   Als je **Ubuntu** gebruikt, dan heb je mogelijk al een oude versie van Python. Check dit door in een terminal het commando `python3 -V` te geven. Misschien heb je dan Python 3.12 of lager. Installeer daarom de nieuwste versie via de "deadsnakes" software repository:

        sudo apt update
        sudo add-apt-repository ppa:deadsnakes/ppa
        sudo apt install python3.14

    - Als je het hebt geïnstalleerd moet je waarschijnlijk vanaf nu het commando `python3.14 -V` gebruiken om de nieuwste versie te starten.

-   Als je met **macOS** werkt, dan heb je waarschijnlijk al Python. Check dit door in een terminal het commando `python3 -V` te geven. Misschien heb je Python 3.12 of lager. In dat geval is het aan te raden een nieuwe versie te installeren, en liefst Python 3.14.

    Als je gaat installeren, doe dit dan door op de Python-homepage een Python installer te downloaden en uit te voeren: <https://www.python.org/ftp/python/3.14.0/python-3.14.0-macos11.pkg>. Hiermee heb je meteen de nieuwste versie.

-   Als je met **Windows** werkt, dan heb je misschien al Python. Check dit door in de command prompt (`cmd.exe`) het commando `python -V` te geven. Misschien heb je Python 3.12 of lager. In dat geval is het aan te raden een nieuwe versie te installeren, en liefst Python 3.14.

    - Het kan ook zijn dat je het commando `py -V` moet gebruiken.

    Als je gaat installeren, doe dit dan door op de Python-homepage een Python installer te downloaden en uit te voeren: <https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe>. Hiermee heb je meteen de nieuwste versie.

    **Kies "Add python to PATH" tijdens de eerste stap van de installatie.**

## Een editor

1. Download de [Pulsar editor](https://pulsar-edit.dev) en installeer volgens de instructies.

    * Kies een **Regular** release van de editor.

2. Maak **altijd** een speciale directory om aan je Python-opdrachten te werken, liefst een directory die automatisch wordt gebackupt (Dropbox, Surfdrive, Onedrive, enz.).

3. Als je Pulsar hebt opgestart, kies dan "Add Project Folder" (staat in het menu File) en kies de directory die je hebt aangemaakt om aan dit vak te werken. Alle schermpjes in Pulsar die je niet nodig hebt kun je sluiten.

## Programma's runnen

Als je Windows gebruikt, bekijk dan eventueel dit filmpje om te zien hoe je Python-programma's kunnen runnen:

![embed](https://www.youtube-nocookie.com/embed/Shf5m_Uol9g?si=mk9nAQ29zSPLtw_s)

Bewaar je Python-bestanden niet op de desktop! Maak een map in Onedrive of ergens anders waar automatisch een backup gemaakt wordt.
