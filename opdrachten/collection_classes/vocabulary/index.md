# Opdracht: Bouw een `VocabularyTrainer`-klasse

## 1. Doel van de opdracht
Ontwerp en implementeer een Python-klasse `VocabularyTrainer` die woorden en hun vertalingen beheert, en waarmee de gebruiker een trainingssessie kan uitvoeren. De klasse gebruikt één of meer Python-collecties om de interne data op te slaan.

## 2. Functionele eisen

### A. Datarepresentatie
De klasse bevat een interne datastructuur voor vocabulaire. Mogelijke keuzes:
- een dictionary met `woord → vertaling(en)`
- een lijst van tuples
- een combinatie van meerdere collecties

Minimaal moet je kunnen:
- woorden toevoegen
- woorden verwijderen
- woorden opvragen

### B. Basisoperaties (CRUD)
De volgende methoden moeten worden geïmplementeerd:

1. **`add_word(word, translation)`**  
   Voegt een woord en vertaling toe. Gaat netjes om met dubbele invoer.

2. **`remove_word(word)`**  
   Verwijdert het woord en alle gekoppelde vertalingen.

3. **`get_translation(word)`**  
   Geeft de vertaling(en) terug, of een melding als het woord niet bestaat.

4. **`list_words()`**  
   Retourneert een overzicht van alle woorden.

### C. Trainingsfunctionaliteit
Implementeer:

**`train(n_questions=5)`**
- Selecteert willekeurige woorden.
- Stelt per woord een quizvraag.
- Controleert of het antwoord klopt.
- Houdt score bij en toont een eindrapport.

Optioneel:
- Meerdere richtingen (NL→EN / EN→NL)
- Ondersteuning voor meerdere juiste vertalingen
- Bijhouden van foutpercentage per woord

## 3. Testbare gedragingen
Demonstreer minimaal:
1. Een trainer aanmaken en woorden toevoegen.
2. Een woord opzoeken.
3. Een woord verwijderen.
4. Alle woorden weergeven.
5. Een trainingssessie uitvoeren.

## 4. Technische randvoorwaarden
- Gebruik één of meer Python-collecties.
- Plaats data in de klasse en gedrag in methoden.
- Voorzie methoden van docstrings.
- Gebruik `random` voor het selecteren van woorden.

## 5. Inleververeisten
- Een bestand `VocabularyTrainer.py` met de klasse.
- Een demonstratiescript of notebook.
- Korte reflectie: motivatie voor de gekozen datastructuur.
