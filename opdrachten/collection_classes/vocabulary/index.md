# Woordjes leren

Ontwerp en implementeer een Python-klasse `VocabularyTrainer` die woorden en hun vertalingen beheert, en waarmee de gebruiker een trainingssessie kan uitvoeren. De klasse gebruikt één of meer Python-collecties om de interne data op te slaan.

## Datarepresentatie

De klasse bevat een interne datastructuur voor het vocabulair. Mogelijke keuzes:

- een dictionary met `woord → vertaling(en)`
- een lijst van tuples
- een combinatie van meerdere collecties

## Basisoperaties

De volgende methoden moeten worden geïmplementeerd:

1. `add_word(word, translation)`
   
   Voegt een woord en vertaling toe. Gaat netjes om met dubbele invoer.

2. `remove_word(word)`
   
   Verwijdert het woord en alle gekoppelde vertalingen.

3. `get_translation(word)`
   
   Geeft de vertaling(en) terug, of een melding als het woord niet bestaat.

4. `list_words()`

   Retourneert een overzicht van alle woorden.

## Trainingsfunctionaliteit

Implementeer de methode `train(n_questions=5)`.

- Selecteert willekeurige woorden.
- Stelt per woord een quizvraag.
- Controleert of het antwoord klopt.
- Houdt score bij en toont een eindrapport.

## Technische randvoorwaarden

- Gebruik `random` voor het selecteren van woorden.
