import copy

def main():
    agenda  = {'januari': [], 'februari': []} # lege agenda met 'januari' en 'februari'

    # de bands
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

def print_agenda(agenda):
    """ Print de agenda """
    print("==== AGENDA ====")
    for month, bands in agenda.items():
        print("maand:", month)
        for index, band in enumerate(bands):
            print(f"  week{index+1} {band}")

def opdracht1(agenda, the_rockets, the_dragonflies):
    """ Voeg 'the_rockets' toe in januari week1.
        Voeg 'the_dragonflies' toe in januari week2.
    """
    agenda['januari'].append(the_rockets)
    agenda['januari'].append(the_dragonflies)
    
def opdracht2(agenda, the_rockets, the_dragonflies):
    """ Voeg 'the_rockets' toe in januari week3.
        Voeg 'the_dragonflies' toe in januari week4.
        Voeg 'the_rockets' toe in januari week5.
    """
    
def opdracht3(agenda, the_rockets, the_dragonflies):
    """ Voeg gastartiest 'Thomas' toe aan 'the_rockets' maar alleen in week3. """

def opdracht4(agenda, the_rockets, the_dragonflies):
    """ 'Jim' verandert zijn artiestennaam in 'Jimmi' in alle optredens. """
    
def opdracht5(agenda, the_rockets, the_dragonflies):
    """ In 'februari' roosteren we dezelfde bands als in januari. """
    
def opdracht6(agenda, the_rockets, the_dragonflies):
    """ Voor 'februari' roosteren we maar 4 weken, verwijder week5 in februari maar niet in januari. """
    
def opdracht7(agenda, the_rockets, the_dragonflies):
    """ In 'maart' roosteren we dezelfde bands als in januari, maar in elk 
        optreden voegen we gastartiest 'Maya' toe.
    """

if __name__ == "__main__":
    main()
