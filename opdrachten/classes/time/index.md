# Time

Maak een bestand `time.py` met de class `Time` die een tijdstip voorstelt (uren, minuten, seconden).

    if __name__ == '__main__':
        t = Time("10:31:00")
        print(t + 90)          # 90 seconden later
        print(t - 45)          # 45 seconden eerder
        print(t.next_hour())   # 11:00:00
        print(t.prev_minute()) # 10:30:00

Schrijf zelf een doctest voor elke method.

## Optellen en aftrekken

In de testcode zie je de operators `-` en `+`. Jouw class moet twee speciale methodes implementeren zodat deze operators het juiste resultaat geven.

De methode voor plus heet `__add__` en voor min heet `__sub__`. Definieer ze zo:

    def __add__(self, other: 'Time'):
        ...
    
    def __sub__(self, other: 'Time'):
        ...

Implementeer dus zowel `__add__` (voor seconden later) als `__sub__` (voor seconden eerder).

Zorg dat tijdsberekeningen correct omgaan met overgangen van minuten en uren, en dat de tijd altijd binnen 0–23 uur blijft.

- `t + 60` betekent 1 minuut later.
- `t - 3600` betekent 1 uur eerder.
