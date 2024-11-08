# Wachtwoord-generator

Veilige wachtwoorden zijn niet per se moeilijk om te genereren, ze zijn vooral moeilijk te onthouden. Daarom is het handig om een password-manager te gebruiken die automatisch wachtwoorden kan genereren en ook invullen in je webbrowser of in een app.

De wachtwoord-generator van Apple probeert enigszins een balans te vinden tussen sterke wachtwoorden en "onthoudbaarheid". Er zijn misschien wel een paar wachtwoorden die je vaak moet intikken en handig zijn om wel uit je hoofd te kennen. De crux is om "woord-achtige" groepjes letters te genereren zodat deze uitspreekbaar en misschien onthoudbaar zijn.

Zie deze blogpost voor meer informatie over de wachtwoorden die zo in elkaar zitten: <https://rmondello.com/2024/10/07/apple-passwords-generated-strong-password-format/>

## Opdracht

Schrijf, in een bestand genaamd `pwdgen.py`, een programma dat een nieuw gegenereerd wachtwoord uitprint, volgens de ideeën uit de blogpost. Voorbeeldoutput:

    $ python3 pwdgen.py
    funrus-Hommez-kajzo7

Daarnaast moet het programma aantonen wat de *gemiddelde* entropie is van wachtwoorden die uit de generator komen. Hiervoor moet je er 10.000 genereren en dan het gemiddelde nemen. Print het resultaat en vergelijk zelf met de blogpost.

## Code

Ontwerp je code zoals hieronder beschreven. Vul de docstrings aan met doctests en eventueel verdere uitleg.

    def new_password() -> str:
        """
        Genereert een wachtwoord
        """

    def print_avg_entropy() -> None:
        """
        Genereert 10.000 wachtwoorden en berekent gemiddelde entropie
        """

    if __name__ == '__main__':
        print(new_password())
        print("Gemiddelde entropie van 10.000 nieuwe wachtwoorden is:")
        print_avg_entropy()

## Tips

* In Python kun je `random.choice("abc")` aanroepen om random één van de letters a, b of c te kiezen. Hiervoor moet je bovenaan je programma `import random` hebben staan. Gebruik dit voorbeeld om losse tekens uit het wachtwoord te genereren.

* Controleer visueel of de wachtwoorden echt aan de eisen voldoen. Ga daarna pas de entropie berekenen.

* Zoek op hoe je de entropie van een string kunt berekenen en gebruik deze methode in je eigen programma. Als je code copy-paste, vermeld dan een bron (link) in een comment.
