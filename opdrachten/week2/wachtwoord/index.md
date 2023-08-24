# Een veilig wachtwoord

We hebben tegenwoordig voor alles accounts en bij elk account hoort een wachtwoord zodat alleen wij bij onze informatie kunnen.
Aan deze wachtwoorden zitten vaak eisen om te zorgen dat ze niet te makkelijk te raden zijn door kwaadwillende buitenstaanders.

## Opdracht

Schrijf, in een bestand genaamd `wachtwoord.py`, een programma dat de gebruiker vraagt voor een wachtwoord en laat weten of het wachtwoord voldoet aan de eisen. Het wachtwoord moet minimaal voldoen aan de volgende eisen:

* Het moet minstens een hoofdletter en een kleine letter bevatten
* Het moet 8 karakters bevatten
* Het moet een cijfer bevatten

## Code

Er zijn drie eisen waar het wachtwoord aan moet voldoen. Deze eisen kunnen allemaal worden gecontroleerd door middel van losse functies. Omdat je ook moet testen of aan de combinatie van eisen is voldaan, heb je ook nog een vierde functie nodig die de check compleet maakt.

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def check_length(password: str) -> bool:
        """
        Controleer of het wachtwoord minstens 8 karakters bevat.
        """

    def check_letter(password: str) -> bool:
        """
        Controleer of het wachtwoord zowel een grote als een kleine letter bevat.
        """

    def check_number(password: str) -> bool:
        """
        Controleer of het wachtwoord een cijfer bevat.
        """

    def check_password(password: str) -> bool:
        """
        Controleer of aan alledrie de eisen is voldaan.
        """

    if __name__ == '__main__':
        <Hoofdprogramma mag maar één functie aanroepen>

## Tips

* Wees creatief bij het implementeren van de drie checks! Er zijn superveel verschillende mogelijkheden om dat voor elkaar te krijgen. Kijk naar alle mogelijke string-operaties in het boek voor inspiratie.
* Let op! Wanneer je checkt of een wachtwoord zowel een grote als een kleine letter bevat, moet je ook checken of het überhaupt een letter bevat.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python wachtwoord.py
    Geef een wachtwoord: AardappelTester123
    Het gegeven wachtwoord is valide.

    $ python wachtwoord.py
    Geef een wachtwoord: hoi
    Het gegeven wachtwoord is niet valide.

## Extra uitdaging

Als extra uitdaging mag je meer eisen bedenken waar het wachtwoord aan moet voldoen. Behalve dat wachtwoorden bepaalde elementen moet bevatten kan je ook dingen verbieden. Zoals dat er geen spaties mogen zijn bijvoorbeeld.

Dit is de laatste opdracht van de week. Mocht je tijd over hebben, kijk dan ook of je kan implementeren dat er wordt weergegeven aan **welke eis** een niet valide wachtwoord niet voldoet, omdat de gebruiker anders niet zoveel kan met de feedback.

Let op: dit is niet verplicht en wordt dus niet automatisch gecheckt.
