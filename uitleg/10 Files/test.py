with open("data.txt", "r") as data_file:
    # gooi eerste regel weg
    data_file.readline()

    # variabelen voor analyse
    gevonden_naam = ''

    # verwerk volgende regels tot einde
    for line in data_file:
        # losse gegevens
        naam, telefoon, teller = line.rstrip().split(',')
        # naam eerder in alfabet of dit is de eerste die we vinden
        if naam < gevonden_naam or gevonden_naam == '':
            # overschrijf gevonden_naam en telefoon met nieuw gevonden
            gevonden_naam = naam
            gevonden_telefoon = telefoon

    # als eerste_naam een waarde bevat hebben we een naam gevonden
    if gevonden_naam != '':
        print(gevonden_telefoon)
