# Transformatie per teken

Maak een Python-module genaamd `char_transformatie.py`. Schrijf de volgende functies met doctests. Je maakt voor deze opgave geen `main`, maar wel doctests!

## Patroon

Je gaat hier steeds een nieuwe string baseren op een gegeven string. Voor elk teken in de gegeven string komt er precies één teken in de nieuwe string: ze zijn dus even lang. Volg dit patroon voor de functies:

    nieuwe_string = ""
    for teken in gegeven_string:
        if ...:
            nieuwe_string += ...
        else:
            nieuwe_string += ...
    return nieuwe_string

Als je op deze manier `if`/`else` gebruikt kun je per teken kiezen uit twee uitkomsten. Je kunt bijvoorbeeld het originele teken houden door te schrijven `nieuwe_string += teken`.

## L337sp34k

Schrijf een functie `l337sp34k` die een string omzet naar "leetspeak". Dat betekent dat een `a` of `A` een `4` wordt, `e/E` worden `3`, `l/L` worden `1`, `o/O` worden `0` en `t/T` worden `7`. Alle andere tekens blijven zoals in het origineel.

## Blackout

Schrijf een functie `blackout` die een string aanneemt en een string teruggeeft waarin elke letter onleesbaar is gemaakt (namelijk vervangen door een `#`).

## Replace char

Schrijf een functie `replace_char` die een string aanneemt en ook nog twee losse tekens `c1` en `c2`. De functie geeft een string terug waarin elk voorkomen van `c1` is vervangen door `c2`.
