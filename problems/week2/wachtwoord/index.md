# Wachtwoord eisen

## Wachtwoorden

We hebben tegenwoordig voor alles accounts en bij elk account hoort een bijbehorend wachtwoord zodat alleen wij bij onze informatie kunnen.
Aan deze wachtwoorden zitten vaak eisen, bijvoorbeeld dat het wachtwoord minstens:
* 8 karakters,
* een hoofdletter en een kleine letter,
* een cijfer,
* een speciaal karakter
moet bevatten.

## Opdracht

Schrijf, in een bestand genaamd `wachtwoord.py`, een programma dat de gebruiker vraagt voor een wachtwoord en laat weten of het wachtwoord voldoet aan de eisen. Het wachtwoord moet minstens voldoen aan de volgende eisen:
* Het moet minstens een hoofdletter en een kleine letter bevatten
* Het moet 8 karakters bevatten
* Het moet een cijfer bevatten

## Code

Er zijn drie eisen waar het wachtwoord aan moet voldoen. Deze eisen kunnen allemaal worden gecontroleerd door middel van losse functies. Omdat je ook moet testen of aan al deze eisen is voldaan heb je ook nog een vierde functie nodig die dat test.

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctest en eventueel verdere uitleg.

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

    def check_password(letter: bool, length: bool, number: bool) -> bool:
        """
        Controleer of aan alle drie de eisen is voldaan.
        """

    if __name__ == '__main__':
        Vraag de gebruiker voor een wachtwoord en controleer met behulp van je zelfgeschreven functies of het wachtwoord aan de eisen voldoet. Print vervolgens of het wachtwoord wel of niet valide is.


## Tips

* Wanneer je checkt of een wachtwoord zowel een grote als een kleine letter bevat, moet je ook checken of het uberhaupt een letter bevat.
* Wees creatief in het bedenken van je checks! Er zijn super veel verschillende mogelijkheden. Kijk bijvoorbeeld naar alle string operaties in het boek voor inspiratie.

## Extra uitdaging

Als extra uitdaging mag je meer eisen waar het wachtwoord aan moet voldoen bedenken. Behalve dat wachtwoorden bepaalde elementen moet bevatten kan je ook dingen verbieden. Zoals dat er geen spaties mogen zijn bijvoorbeeld.
Let op: dit is niet verplicht en wordt dus niet gecheckt met checkpy.

Dit is de laatste opdracht van de week. Mocht je tijd over hebben, kijk dan ook of je kan implementeren dat er wordt weergegeven aan welke eis een niet valide wachtwoord niet voldoet.

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python wachtwoord.py
    Geef een wachtwoord: AardappelTester123
    Het gegeven wachtwoord is valide.

    $ python wachtwoord.py
    Geef een wachtwoord: hoi
    Het gegeven wachtwoord is niet valide.
