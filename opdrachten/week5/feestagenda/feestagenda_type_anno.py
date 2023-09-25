Agenda = dict[str, list[list[str]]]

def main() -> None:
    agenda: Agenda  = {'januari': [], 'februari': []} # lege agenda met 'januari' en 'februari'
    print_agenda(agenda)
    
    # de bands:
    the_rockets     = ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
    the_dragonflies = ['The Dragonflies:', 'Lisa', 'Alexander', 'Lucas']

    # we vullen de agenda in
    print("\nopdracht1:")
    opdracht1(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("\nopdracht2:")
    opdracht2(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("\nopdracht3:")
    opdracht3(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("\nopdracht4:")
    opdracht4(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("\nopdracht5:")
    opdracht5(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("\nopdracht6:")
    opdracht6(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("\nopdracht7:")
    opdracht7(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

def print_agenda(agenda: Agenda) -> None:
    """ Print de agenda """
    print("==== AGENDA ====")
    for month, bands in agenda.items():
        print("maand:", month)
        for index, band in enumerate(bands):
            print(f"  week{index+1} {band}")

def opdracht1(agenda: Agenda, the_rockets: list[str], the_dragonflies: list[str]) -> None:
    """ Voeg 'the_rockets' toe in januari week1.
        Voeg 'the_dragonflies' toe in januari week2.
        kan in 2 regels
    """
    agenda['januari'].append(the_rockets)
    agenda['januari'].append(the_dragonflies)
    
def opdracht2(agenda: Agenda, the_rockets: list[str], the_dragonflies: list[str]) -> None:
    """ Voeg 'the_rockets' toe in januari week3.
        Voeg 'the_dragonflies' toe in januari week4.
        Voeg 'the_rockets' toe in januari week5.
        kan in 3 regels
    """

def opdracht3(agenda: Agenda, the_rockets: list[str], the_dragonflies: list[str]) -> None:
    """ Voeg gastartiest 'Thomas' toe aan 'the_rockets' maar alleen in week3.
        kan in 2 regels
    """

def opdracht4(agenda: Agenda, the_rockets: list[str], the_dragonflies: list[str]) -> None:
    """ 'Jim' verandert zijn artiestennaam in 'Jimmi' in alle optredens.
        kan in 2 regels
    """

def opdracht5(agenda: Agenda, the_rockets: list[str], the_dragonflies: list[str]) -> None:
    """ In 'februari' roosteren we dezelfde bands als in januari.
        kan in 1 regel
    """

def opdracht6(agenda: Agenda, the_rockets: list[str], the_dragonflies: list[str]) -> None:
    """ Voor 'februari' roosteren we maar 4 weken, verwijder week5 in februari maar niet in januari.
        kan in 2 regels
    """

def opdracht7(agenda: Agenda, the_rockets: list[str], the_dragonflies: list[str]) -> None:
    """ In 'maart' roosteren we dezelfde bands als in januari, maar in elk optreden voegen we gastartiest 'Maya' toe.
        kan in 4 regels
    """

if __name__ == "__main__":
    main()
