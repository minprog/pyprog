# RGB

Maak een bestand `rgb.py` met de class `RGB` die een kleur voorstelt als combinatie van rood, groen en blauw (waarden 0 t/m 255).

    if __name__ == '__main__':
        c = RGB(100, 150, 200)
        print(c)
    
        print(c.lighter(0.2))   # iets lichtere kleur
        print(c.darker(0.3))    # iets donkerdere kleur
        print(c.invert())       # omgekeerde kleur
        print(c.to_hex())       # geeft een CSS-kleur, bijvoorbeeld '#6496c8'

Schrijf zelf een doctest voor elke method.

## Formules

- Bij `lighter(factor)` verhoog je elke kleurcomponent met een percentage van de afstand tot 255.  
- Bij `darker(factor)` verlaag je elke component met een percentage van de huidige waarde.  
- Bij `invert()` trek je elke component af van 255.  

Gebruik afronding (`round`) indien nodig, en zorg dat waarden binnen 0--255 blijven.

## Hexadecimale kleur

De methode `to_hex()` maakt een CSS-kleurstring zoals `#6496c8`.

Zet elke losse R, G en B-waarde om naar een hexadecimale string met twee tekens via de ingebouwde Python-functie `hex()`. Helaas krijg je dan altijd een string met `0x` ervoor, bijvoorbeeld `0x64`. Knip dus de juiste informatie eraf en stel de hex-string samen.
