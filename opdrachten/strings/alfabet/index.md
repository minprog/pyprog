# Alfabet

Schrijf een programma `alfabet.py` dat van twee woorden bepaalt welke eerder in het woordenboek voorkomt. Daarbij mag geen verschil worden gemaakt tussen hoofdletters en kleine letters.

## Details

- Vergelijk de woorden letter voor letter (dus in het eerste voorbeeld ga je eerst de `T` en de `L` vergelijken).

- Het algoritme moet zo weinig mogelijk letters bekijken, en zo snel mogelijk de conclusie trekken welk woord eerder komt.

- Je mag dus niet eerst de hele strings lowercase maken of de hele strings vergelijken.

## Code

Ontwerp je code zoals hieronder beschreven. Schrijf de docstring, doctests en het hoofdprogramma.

    def comes_before(word1: str, word2: str) -> bool:
        """
        
        """

    if __name__ == '__main__':
        <Hoofdprogramma>

## Voorbeelden

Je programma moet uiteindelijk werken zoals in de voorbeelden hieronder.

    $ python3 alfabet.py
    Woord 1: Taylor
    Woord 2: Lana
    Lana first

    $ python3 alfabet
    Woord 1: shark
    Woord 2: sWoRd
    shark first

    $ python3 alfabet
    Woord 1: Daantje
    Woord 2: Daan
    Daan first

    $ python3 alfabet
    Woord 1: amanda
    Woord 2: Amanda
    No need to decide!
