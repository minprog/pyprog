import copy

def main():
    agenda = {'januari': [], 'februari': []} # lege agenda met 'januari' en 'februari'
    print_agenda(agenda)
    
    # de bands:
    the_rockets     = ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
    the_dragonflies = ['The Dragonflies:', 'Lisa', 'Alexander', 'Lucas']

    # we vullen de agenda in
    print("opdracht1:")
    opdracht1(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("opdracht2:")
    opdracht2(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("opdracht3:")
    opdracht3(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("opdracht4:")
    opdracht4(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("opdracht5:")
    opdracht5(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("opdracht6:")
    opdracht6(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)

    print("opdracht7:")
    opdracht7(agenda, the_rockets, the_dragonflies)
    print_agenda(agenda)


def print_agenda(agenda) -> None:
    """ Print de agenda """
    print("==== AGENDA ====")
    for month, bands in agenda.items():
        print("maand:", month)
        for index, band in enumerate(bands):
            print(f"  week{index+1} {band}")

def opdracht1(agenda, the_rockets, the_dragonflies) -> None:
    """ Voeg 'the_rockets' toe in januari week1.
        Voeg 'the_dragonflies' toe in januari week2.
    """
    agenda['januari'].append(the_rockets)
    agenda['januari'].append(the_dragonflies)

def opdracht2(agenda, the_rockets, the_dragonflies) -> None:
    """ Voeg 'the_rockets' toe in januari week3.
        Voeg 'the_dragonflies' toe in januari week4.
        Voeg 'the_rockets' toe in januari week5.
    """
    agenda['januari'].append(the_rockets)
    agenda['januari'].append(the_dragonflies)
    agenda['januari'].append(the_rockets)

def opdracht3(agenda, the_rockets, the_dragonflies) -> None:
    """ 'Lisa' verandert haar artiestennaam in 'LiZA' in alle optredens.
        Pas het rooster aan.
    """
    the_dragonflies[1] = 'LiZa'
    
def opdracht4(agenda, the_rockets, the_dragonflies) -> None:
    """ Voeg gastartiest 'Thomas' toe aan 'the_rockets' maar alleen in week3.
    """
    agenda['januari'][2] = copy.copy(the_rockets)
    agenda['januari'][2].append('Thomas') 

def opdracht5(agenda, the_rockets, the_dragonflies) -> None:
    """ In 'februari' roosteren we dezelfde bands als in januari.
    """
    agenda['februari'] = agenda['januari'] 

def opdracht6(agenda, the_rockets, the_dragonflies) -> None:
    """ Voor 'februari' roosteren we maar 4 weken, verwijder week5 in februari maar niet in januari.
    """
    agenda['februari'] = copy.copy(agenda['januari'])
    agenda['februari'].pop()

def opdracht7(agenda, the_rockets, the_dragonflies) -> None:
    """ In 'maart' roosteren we dezelfde bands als in januari, maar in elk optreden voegen we gastartiest 'Maya' toe. 
    """
    agenda['maart'] = copy.deepcopy(agenda['januari'])
    agenda['maart'][0].append('Maya')
    agenda['maart'][1].append('Maya')
    agenda['maart'][2].append('Maya')

if __name__ == "__main__":
    main()
