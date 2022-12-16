# -------------------------------------------------------------------------
# Opdracht: String & Files CO2 (alternatieve uitwerking)
# de andere uitwerking staat in voorbeelden deel 1

def co2_average(filename: str) -> float:
    """
    Berekent het gemiddelde van de waardes

    >>> co2_average('CO2.txt')
    700.2
    """
    data = []

    with open(filename) as f:
        for line in f:
            hour, ppm = line.strip().split(',')
            # we splitten maar we gaan "hour" niet opslaan omdat we die 
            # niet gebruiken
            # let op dat hier alvast een int() conversie wordt gedaan
            data.append(int(ppm))

    # werkt alleen met de data-waarden, niet met de uren
    vals = data
    return sum(vals) / len(vals)

def co2_largest_increase(filename: str) -> int:
    """
    Geeft het uur met de grootste stijging in ppm aan

    >>> co2_largest_increase('CO2.txt')
    6
    """
    hours = []
    data = []

    with open(filename) as f:
        for line in f:
            hour, ppm = line.strip().split(',')
            # let op dat hier alvast een int() conversie wordt gedaan
            hours.append(int(hour))
            data.append(int(ppm))

    # we houden bij op welke plek *tot nu toe* de grootste
    # stijging plaatsvond
    largest_increase_until_now = -1
    place_of_largest_increase = 0

    # gebruik een index om langs alle data te lopen
    # zodat we weten "waar we zijn"
    # begin bij 1 niet bij 0, zodat we de stijging
    # met de "vorige" kunnen berekenen (bij het eerste
    # datapunt is er nog geen "vorige")
    for i in range(1, len(hours)):
        # verschil huidige en vorige regel
        diff = data[i] - data[i-1]
        
        # opslaan als groter dan vorige stijging
        if diff > largest_increase_until_now:
            largest_increase_until_now = diff
            place_of_largest_increase = i

    return hours[place_of_largest_increase]

# -------------------------------------------------------------------------
# Opdracht: Classes / Secret message

class SecretMessage:
    """
    Class voor een geheime boodschap
    """
    def __init__(self, code: str, message: str):
        """
        Slaat argumenten op
        """
        self._code = code
        self._message = message

    def open(self, code: str) -> str:
        """
        Checkt of code correct is en geeft eventueel boodschap terug
        >>> code = SecretMessage('1234', 'Hi')
        >>> code.open('12345')
        'Incorrect code'
        >>> code.open('1234')
        'Hi'
        """
        if code == self._code:
            return self._message
        return "Incorrect code"

    def changeCode(self, old_code: str, new_code: str) -> bool:
        """
        Verandert code als de oude code goed wordt opgegeven
        
        >>> code = SecretMessage('1234', 'Hi')
        >>> code.changeCode('1234', 'geheim')
        True
        >>> code = SecretMessage('1234', 'Hi')
        >>> code.changeCode('5820', 'geheim')
        False
        """
        if self._code == old_code:
            self._code = new_code
            return True
        return False

# -------------------------------------------------------------------------
# Opdracht: Classes / Secret message

class Student:
    """
    Deze class is niet goed testbaar met doctest omdat deze geen methodes 
    heeft. Zoals in de opdracht staat is er wel een apart stuk code om
    de class te gebruiken, dus dat demonstreert uiteindelijk ook de werking.
    """
    def __init__(self, name: str, student_number: int, status: int):
        self.name = name
        self.student_number = student_number
        self.status = status

import random

def create_and_print_first_year():
    """
    Maak 20 random gevulde studenten en print een lijst van 1e-jaars
    Hier is wel een doctest gebruikt, waarvoor de randomizer wordt
    "uitgezet" door een seed 0 in te voeren (hierdoor komen er steeds
    dezelfde "random" waarden uit als je de code runt).
    >>> random.seed(0)
    >>> create_and_print_first_year()
    Student10
    Student13
    Student14
    Student16
    """

    students = []

    for number in range(1, 21):
        name = "Student" + str(number)
        # random studentennummer uit de range [1, 1000]
        # we hebben zelf bedacht dat een studentnummer er zo uitziet,
        # het maakt niet zoveel uit, er staan geen eisen in de opdracht
        student_number = random.randint(1, 1000)

        # random jaar uit de range [1, 4]
        year = random.randint(1, 4)

        # maak het Student object en voeg die toe aan de lijst
        new_student = Student(name, student_number, year)
        students.append(new_student)

    for student in students:
        # check of de student in het 1e jaar zit
        if student.status == 1:
            print(student.name)

# -------------------------------------------------------------------------
# Opdracht: Comprehensions

def list_to_string(input_list: list) -> str:
    """
    Converteert een lijst naar een string-representatie.
    Let op dat er in het voorbeeld in de opgaven geen spaties in 
    het resultaat staan, dus hier ook niet.

    >>> list_to_string([1,2,3])
    '1,2,3'
    >>> list_to_string([0,0,0,0,0])
    '0,0,0,0,0'
    """
    return ",".join([str(n) for n in input_list])

# -------------------------------------------------------------------------
# Opdracht: Users
#
# Deze implementatie is *zonder* classes maar *met* dictionaries.
# Een opdracht als deze kan op vele verschillende manieren gemaakt worden;
# het is aan te raden om de opdracht werken te maken op een manier die
# voor jou "goed te doen" is. Daarna kun je altijd nog kijken of je 
# er een class omheen kunt bouwen, of de datastructuur aanpassen van lists
# naar dictionary of iets anders.
#
#
# Over de inhoud van de opdracht: je kende waarschijnlijk niet het fenomeen
# van een passwd-file. Probeer daarom scherp te lezen welke informatie
# je hebt uit de opdracht. Als je iets niet begrijpt, maak dan zelf een keuze
# hoe je het implementeert. Het is niet erg als het een beetje anders is
# dan wij in gedachten hadden. Als het maar interessante en correcte code 
# oplevert waarvan jij met doctests aantoont dat het werkt.

COLUMN_PASSWORD = 0
COLUMN_USER_ID = 1
COLUMN_SHELL = 5
PRIVILEGED_START = 0
PRIVILEGED_END = 100
VALID_SHELLS = ['/usr/bin/false', '/bin/sh', '/bin/zsh', '/binotto/mattia']

def load(filename: str) -> dict:
    """
    Laad data in uit een file met account-gegevens,
    return als een dictionary. 
    De key is de username, en als value zijn daar de overige gegevens
    aan gekoppeld.

    >>> load("passwd")
    {'nobody': ['*', '-2', '-2', 'Unprivileged User', '/var/empty', '/usr/bin/false'], 'root': ['*', '0', '0', 'System Administrator', '/var/root', '/bin/sh'], 'daemon': ['*', '1', '1', 'System Services', '/var/root', '/usr/bin/false'], 'joedoe': ['*', '1000', '1000', 'Joe Dough', '/Users/joe', '/bin/zsh']}
    """

    with open(filename, "r") as f:
        lines = f.readlines()

    user_dict = {}

    for line in lines:
        values = line.split(":")
        values_stripped = [value.strip() for value in values]
        username = values_stripped[0]

        user_dict[username] = values_stripped[1:]

    return user_dict

def users(user_dict: dict) -> list:
    """
    Geef alle namen van gebruikers uit een user list.
    Omdat wij een dictionary gebruiken kunnen we de lijst
    er zo uithalen met hulp van de methode keys().

    Let op dat we hier in de doctest de variabele user_data
    gebruiken die in de vorige doctest is aangemaakt!
    >>> user_data = load("passwd")
    >>> users(user_data)
    ['nobody', 'root', 'daemon', 'joedoe']
    """

    usernames = list(user_dict.keys())
    return usernames

def priviliged_users(user_dict: dict) -> list:
    """
    <zinnige docstring hier>

    >>> user_data = load("passwd")
    >>> priviliged_users(user_data)
    ['root', 'daemon']
    """

    usernames = []

    # iterate over de waardes in de gegeven dict
    for name, values in user_dict.items():
        user_id = int(values[COLUMN_USER_ID])

        # kijk of de user id geprivileged is
        if user_id in range(PRIVILEGED_START, PRIVILEGED_END + 1):
            usernames.append(name)

    return usernames


def chpass(user_dict: dict, username: str, old_password: str, new_password: str) -> bool:
    """
    Wijzigt het wachtwoord van de user, dat is element 0 uit de list
    van user data.
    >>> user_data = load("passwd")
    >>> chpass(user_data, 'root', 'wrong_old_password', 'invalid')
    False
    >>> chpass(user_data, 'root', '*', 'new_password')
    True
    >>> user_data['root'][0] == 'new_password'
    True
    """

    # check of de username bestaat
    if username not in user_dict:
        return False

    # check het wachtwoord
    if user_dict[username][COLUMN_PASSWORD] != old_password:
        return False

    # verander het wachtwoord
    user_dict[username][COLUMN_PASSWORD] = new_password

    return True


def chsh(user_dict: dict, username: str, shell: str) -> bool:
    """
    Wijzigt de "shell" van de user, dat is element 5 uit de list
    van user data. In de tests hieronder checken we niet alleen
    of er True/False uitkomt, maar bij True checken we daarna
    ook nog of de waarde echt is aangepast in de data.
    
    >>> user_data = load("passwd")
    >>> chsh(user_data, 'root', 'invalid')
    False
    >>> chsh(user_data, 'root', '/bin/zsh')
    True
    >>> user_data['root'][5] == '/bin/zsh'
    True
    """

    # check of de username bestaat
    if username not in user_dict:
        return False

    # check of de shell geldig is
    if shell not in VALID_SHELLS:
        return False

    # update de shell
    user_dict[username][COLUMN_SHELL] = shell

    return True
