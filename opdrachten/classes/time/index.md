# Time

Maak een bestand `time.py` met de class `Time` die een tijdstip voorstelt (uren, minuten, seconden).

    if __name__ == '__main__':
        t = Time("10:31:00")
        print(t + 90)          # 90 seconden later
        print(t - 45)          # 45 seconden eerder
        print(t.next_hour())   # 11:00:00
        print(t.prev_minute()) # 10:30:00
        print(t)               # nog steeds 10:31:00

De methoden van deze class mogen de interne waarden (instance variables) niet veranderen! Ook bij deze opdracht berekent zo'n methode de nieuwe waarde, maakt een nieuw object en returnt dat object.

Schrijf zelf een doctest voor elke method.

## Optellen en aftrekken

In de testcode zie je de operators `-` en `+`. Jouw class moet twee speciale methodes implementeren zodat deze operators het juiste resultaat geven.

De methode voor plus heet `__add__` en voor min heet `__sub__`. Definieer ze zo:

    def __add__(self, other: int):
        ...
    
    def __sub__(self, other: int):
        ...

Let op dat je dus geen `Time`-object meekrijgt als `other`, maar een simpele `int`.

## Hints

1. Gebruik een interne representatie van *seconden*, zodat je makkelijk berekeningen kunt doen. Hier is een methode die de tijd omzet naar seconden:

        def to_seconds(self) -> int:
            return self.hours * 3600 + self.minutes * 60 + self.seconds

2. Zorg dat alle tijdsberekeningen correct omgaan met overgangen van minuten en uren, en dat de tijd altijd binnen 0–23 uur blijft.

    - `t + 60` betekent 1 minuut later.
    - `t - 3600` betekent 1 uur eerder.
