# Kunstroof
Er heeft een kunstroof plaatsgevonden in het nationale kunstmuseum van
Waddinxveen.  De politie ziet om te beginnen alle inwoners als
mogelijke dader. In bestand [inwoners.csv](inwoners.csv) vind je de
ids en namen van alle (200.000) inwoners.

Het is jouw taak om voor de politie de groep van mogelijke daders zo
klein mogeliik te maken op basis van onderstaande informatie.


## Buitenland
Mensen die in het buitenland waren ten tijden van de kunstroof zijn
geen daders. De id van deze mensen vind je in bestand
[buitenland.csv](buitenland.csv).

**opdracht1**: Bepaal de ids van de nog mogelijke daders. Gebruik
hierbij eerst een `list` om de ids op te slaan en op te zoeken.

tip: gebruik Python module 'cvs' om makkelijker csv files te lezen

test: Er zouden nog 183.745 mogelijke daders moeten overblijven.

**opdracht2**: Het zoeken in een `list` is traag, gebruik daarom nu
een `set` om de ids op te slaan en op te zoeken voor hogere snelheid.

tip: Controlleer of het type van de verzameling echt een `set` is door
het type te printen, bv met: print(type(dader_ids)).

- Hoeveel sneller is een 'set'?
- Waarom is een 'set' sneller?

**opdracht3**: Het is nog iets sneller, makkelijker en leesbaarder
om [set operatoren](https://docs.python.org/2/library/sets.html) te
gebruiken:

- methode `union()`, of de '|' operator
- methode `intersection()`, of de '&' operator
- methode `difference()`, of de '-' operator
- methode `symmetric_difference()`, of de '^' operator

## Lengte
Met beveiligingscamera's is vastgesteld dat de dader een lengte heeft
groter of gelijk aan 150 en kleiner of gelijk aan 160. De lengte van
inwoners vind je in bestand [lengte.csv](lengte.csv).

**opdracht4**: Wat zijn nu de ids van de nog mogelijke daders?

test: Er zouden nog 49.130 mogelijke daders moeten overblijven.

## Geboortedatum
Op basis van getuigenverklaringen is vastgesteld dat de dader geboren
is op of na 1980 en op of voor 1990. De geboortedata van inwoners vind
je in bestand [geboortedatum.csv](geboortedatum.csv).

**opdracht5**: Wat zijn nu de ids van de nog mogelijke daders?

tip: Probeer waar mogelijk code-duplicatie te voorkomen door
herbruikbare functies te maken.

test: Er zouden nog 9643 mogelijke daders moeten overblijven.

## Beroepscrimineel of Gelegenheidsdief
De politie neemt aan dat de dader een beroepscrimineel is die al
eerder in contact is gekomen met justitie, **of** dat het een
gelegenheidsdief is die binnen 50km van het museum woont. Het museum
bevindt zich op GPS coordinaat lengtegraad:52.0408703,
breedtegraad:4.6603396.

De ids van beroepscriminelen die al eerder in contact zijn gekomen met
justitie vind je in bestand
[beroepscrimineel.csv](beroepscrimineel.csv).

De postcodes van inwoners vind je in bestand
[postcode.csv](postcode.csv).

De GPS coordinaten van iedere postcode vind je in bestand
[postcode_coordinaat.csv](postcode_coordinaat.csv).

### 'geopy'
Gebruik Python module 'geopy' om afstanden tussen GPS coordinaten te
bepalen. Installeer deze module met:

```
pip install geopy
```

Vervolgens kun je op deze manier de afstand tussen Amsterdam en Parijs
bepalen:

```
from geopy.distance import distance as geopy_distance

coord1 = (52.372947, 4.893291) # Amsterdam
coord2 = (48.857891, 2.295166) # Parijs

print(geopy_distance(coord1, coord2).km)  # distance in kilometers
```

**opdracht6**: Wat zijn nu de nog mogelijke daders?

tip: Gebruik een 'dict' om snel op postcode te kunnen zoeken.

test: Er zouden nog 2716 mogelijke daders moeten overblijven.

# Resultaat
Reporteer je resultaat.

**opdracht7**: Maak een csv file 'daders.csv' van de nog mogelijke
daders met 'id, naam' als header.
