# Uitwerking oefententamen Programmeren (deel 1)
# gemaakt door docenten en assistenten
#
# Er zijn heel veel manieren om programmeeropdrachten te maken. Als de
# uitkomst correct is (aangetoond met diverse doctests) dan kan de
# uitwerking meetellen. Daarnaast wordt gelet op goed gebruik van allerlei
# constructies die je hebt geleerd, zoals functies, lijsten, dictionaries
# comprehensions en classes.

# -------------------------------------------------------------------------
# Opdracht: vakantie

def vakantie(days: int, vervoer: str) -> int:
    """
    Bereken de vakantiekosten. Dit zijn een beetje weinig doctests.
    Met onderstaande 2 doctests is redelijk duidelijk dat de opdracht
    goed werkt, maar om echt goed te testen zal er zeker ook gecheckt
    moeten worden of het ook met 0 dagen werkt, en of het met auto
    een correct totaal geeft.

    >>> vakantie(1, "v")
    319
    >>> vakantie(10, "trein")
    1648
    """

    # verblijfkosten
    cost = days * 60

    # reiskosten
    if vervoer == 'v':
        cost += days * 250
    elif vervoer == 'a':
        cost += days * 150
    else:
        cost += days * 100

    # servicekosten
    cost += int(cost * 0.03)

    return cost

# -------------------------------------------------------------------------
# Opdracht: Hoofdletters

def count_capitalized_words(text: str) -> int:
    """
    Tel de woorden met hoofdletter. Er zijn wat specifieke eisen in
    de opdracht, maar in de praktijk kun je toch vrij snel tellen
    nadat je split() hebt gebruikt.

    De doctests hieronder zijn de voorbeelden uit de opdracht, maar als er
    geen voorbeelden in de opdracht staan kun je voorbeelden verzinnen
    op basis van de omschrijving van wat er wel/niet geteld moet
    worden.

    >>> count_capitalized_words("Er zijn geen goede schrijvers.")
    1
    >>> count_capitalized_words("Obi-Wan Kenobi nam zijn taak vrij serieus")
    2
    >>> count_capitalized_words("bell hooks wrote on race, feminism and class.")
    0
    """

    words = text.split()

    # begin bij 0 woorden, daarna tellen in de loop
    count_capitalized = 0

    for word in words:
        # check of de eerste letter een hoofdletter is
        if word[0].isupper():
            count_capitalized += 1

    return count_capitalized

    # alternatief met list comprehensions:
    # maakt een lijst met woorden met hoofdletter en telt dan het aantal
    # count_capitalized = len([word for word in text.split(' ') if word[0].isupper()])

# -------------------------------------------------------------------------
# Opdracht: Email-validator

def validate_email(address: str) -> bool:
    """
    Deze eerste uitwerking van de opdracht bestaat uit maar liefst
    4 functies. Elke functie doet een klein deel van het werk
    en wordt apart getest. Dit wordt gewaardeerd

    >>> validate_email("m.stegeman@uva.nl")
    True
    >>> validate_email("m@uva")
    False
    >>> validate_email("@uva.nl")
    False
    >>> validate_email("martijn")
    False
    """

    return (email_contains_at(address) and
            email_container_at_least_letter_in_username(address) and
            email_dot_in_domain(address))

def email_contains_at(address: str) -> bool:
    """
    Checkt of een mailadres (of eigenlijk een string) een @ bevat.

    >>> email_contains_at("")
    False
    >>> email_contains_at("§")
    False
    >>> email_contains_at("@")
    True
    >>> email_contains_at("@uva.nl")
    True
    >>> email_contains_at("m.stegeman@uva.nl")
    True
    """

    return "@" in address

def email_container_at_least_letter_in_username(address: str) -> bool:
    """
    Krijgt een mailadres met een @ erin, en checkt
    of er minstens één letter in het deel vóór de @ staat.

    >>> email_container_at_least_letter_in_username("@uva.nl")
    False
    >>> email_container_at_least_letter_in_username("1@uva.nl")
    False
    >>> email_container_at_least_letter_in_username("@@@uva.nl")
    False
    """

    # Let op, de laatste test hierboven met @@@ test iets dat niet in
    # de opdracht staat! Hierdoor is onderstaande code ingewikkelder
    # geworden dan nodig is. Pas dus op met toevoegen van doctests die
    # iets testen dat niet in het opdracht staat!

    # zoek de @ in de string
    # we nemen aan dat deze aanwezig is om dat altijd
    # eerst de functie "email_contains_at" wordt gecheckt
    at_location = address.index("@")

    # neem alle tekens vóór de @
    username = address[:at_location]

    for letter in username:
        if letter.isalpha():
            # als we de eerste letter vinden is het al goed
            return True

    # niks gevonden, dan niet goed
    return False

def email_dot_in_domain(address: str) -> bool:
    """
    Krijgt een mailadres met een @ erin, en checkt
    of er een . in het deel na de @ staat.

    >>> email_dot_in_domain("martijn@uva.nl")
    True
    >>> email_dot_in_domain("martijn@uva")
    False
    """

    # zoek de @ in de string
    at_location = address.index("@")

    # neem alle tekens na de @
    domain = address[at_location+1:]

    return "." in domain

# -------------------------------------------------------------------------
# Opdracht: Email-validator (UITWERKING 2)

def valideer_mail(adres: str) -> bool:
    """
    Deze uitwerking bevat slechts één functie. De uitwerking is
    net zo correct als de uitwerking hierboven, en is min of meer
    op de zelfde code gebaseerd. Alleen wordt het goed gebruiken
    en opsplitsen van functies niet gedemonstreerd.

    >>> valideer_mail("martijn@uva.nl")
    True
    >>> valideer_mail("martijn")
    False
    >>> valideer_mail("98@uva.nl")
    False
    >>> valideer_mail("98@uva")
    False
    >>> valideer_mail("martijn@uva")
    False
    """

    # indien geen @ dan meteen fout
    if not "@" in adres:
        return False

    # deze uitwerking heeft geen doctest met @@@ erin, dus
    # in dit geval kan gewoon split gebruikt worden
    username, domain = adres.split("@")

    # tel aantal letters vóór de @
    aantal_letters_in_username = 0
    for letter in username:
        if letter.isalpha():
            aantal_letters_in_username += 1

    # indien geen letters dan meteen fout
    if aantal_letters_in_username == 0:
        return False

    # indien geen . na de @, dan fout
    if not "." in domain:
        return False

    # als we nu nog hier zijn, dan is het mailadres goedgekeurd
    return True

# -------------------------------------------------------------------------
# Opdracht: String & Files PREFIX

def is_prefix(string1: str, string2: str) -> bool:
    """
    <zinnige docstring hier>

    >>> is_prefix("bob", "bobmarley")
    True
    >>> is_prefix("1234", "123")
    False
    >>> is_prefix("jaja", "ajajaja")
    False
    """

    # als string1 een prefix moet zijn van string2,
    # dan mag deze dus sowieso niet langer zijn dan string2
    if len(string1) > len(string2):
        return False

    # check voor elke letter in string1 of deze op dezelfde plaats staat
    # in string2
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False

    return True

# -------------------------------------------------------------------------
# Opdracht: String & Files PREFIX

def checksum(file_name: str) -> int:
    """
    We gebruiken hier de file CO2.txt die we voor de volgende opdracht toch
    moeten aanmaken.

    In principe is één doctest hier wel genoeg. Bij het tentamen zal
    aangegeven worden welke file je moet maken om te testen.

    >>> checksum('CO2.txt')
    2649
    """
    checksum_total = 0

    with open(file_name, 'r') as file:
        for line in file:
            for character in line:
                checksum_total += ord(character)

    return checksum_total

# -------------------------------------------------------------------------
# Opdracht: String & Files TEXT COUNT

def text_count(file_name: str) -> list[int]:
    """
    Telt aantal tekens, woorden en regels in een file.

    Deze functie zou je met meerdere bestanden willen testen, dus
    ook met meerdere doctests;
    als zoiets wordt gevraagd op het tentamen geven we aan welke
    doctests je zou moeten hebben. In dit geval laten we de doctests
    daarom nu weg.
    """
    with open(file_name, 'r') as file:
        characters = 0
        words = 0
        lines = 0

        for line in file:
            # de opdracht zegt niet wat meetelt als een "teken" ofwel
            # "character", dus hier tellen we gewoon alles op elke regel
            characters = len(line)

            # woorden kun je meestal gewoon tellen via een split, tenzij
            # in de opdracht een specifieke definitie van een "woord" staat
            # vermeld
            words = len(line.split(' '))

            # de regels
            lines += 1

    # In de opdracht staat dat drie dingen moeten worden teruggegeven
    # maar er staat niet in welk formaat; hier gebruiken we een list.
    return [characters, words, lines]

    # Je zou ook return (characters, words, lines) kunnen doen, dus
    # met een tuple.

# -------------------------------------------------------------------------
# Opdracht: String & Files CO2

# Opmerking bij deze opdracht:
# Als je de opdracht niet goed leest zou je kunnen denken dat
# de datafile één meetwaarde per regel heeft, met een komma erin
# Maar in de opdracht staat dat het een datafile is twee kolommen:
# de eerste kolom is een teller van uren, de tweede kolom (na de komma)
# is de meetwaarde

class CO2:
    """
    C02 data analyzer

    >>> analyzer = CO2("CO2.txt")
    >>> analyzer.average()
    700.2
    >>> analyzer.largest_increase()
    6
    """
    def __init__(self, file: str):
        """
        Leest een databestand in en slaat de waardes op in twee lijsten
        dit is dan de enige plek waar data uit de file wordt ingeladen
        """
        self.hours = []
        self.data = []

        with open(file) as f:
            for line in f:
                hour, ppm = line.strip().split(',')
                # let op dat hier alvast een int() conversie wordt gedaan
                self.hours.append(int(hour))
                self.data.append(int(ppm))

    def average(self) -> float:
        """
        Berekent het gemiddelde van de waardes
        Doctest staat bovenaan bij de class!
        """
        # werkt alleen met de data-waarden, niet met de uren
        vals = self.data
        return sum(vals) / len(vals)

    def largest_increase(self) -> int:
        """
        Geeft het uur met de grootste stijging in ppm aan
        Doctest staat bovenaan bij de class!
        """
        # we houden bij op welke plek *tot nu toe* de grootste
        # stijging plaatsvond
        largest_increase_until_now = -1
        place_of_largest_increase = 0

        # gebruik een index om langs alle data te lopen
        # zodat we weten "waar we zijn"
        # begin bij 1 niet bij 0, zodat we de stijging
        # met de "vorige" kunnen berekenen (bij het eerste
        # datapunt is er nog geen "vorige")
        for i in range(1, len(self.hours)):
            # verschil huidige en vorige regel
            diff = self.data[i] - self.data[i-1]
            
            # opslaan als groter dan vorige stijging
            if diff > largest_increase_until_now:
                largest_increase_until_now = diff
                place_of_largest_increase = i

        return self.hours[place_of_largest_increase]
