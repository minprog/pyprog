# War

> Let op! Bij deze opdracht schrijf je tests middels het Pytest-framework en niet als doctests.

Implementeer het kaartspel oorlogje ([war](https://www.youtube.com/watch?v=01-2pNCZiNk)) voor twee spelers. Dit zijn de spelregels:

1. Alle 52 kaarten worden gehusseld en verdeeld over twee stapels. 
2. In elke ronde trekken beide spelers de bovenste kaart van hun stapel.
3. De speler met de hoogste kaart wint, neemt beide kaarten en legt deze onderaan hun stapel.
    1. Als de ene speler een aas heeft (hoogste waarde) en de andere speler een twee (laagste waarde), dan wint de speler met de twee.*
4. Bij gelijkspel houden beide spelers hun kaarten en leggen deze onderaan hun stapel.
5. Het spel gaat door totdat één speler geen kaarten meer heeft.
    1. Als het spel te lang duurt, 1000 rondes of meer, dan stopt het spel.
6. De speler met de meeste kaarten aan het einde wint.

Dit zijn de waardes van iedere kaart, de kaartsymbolen maken niet uit:

* 2 = 2
* 3 = 3
* 4 = 4
* 5 = 5
* 6 = 6
* 7 = 7
* 8 = 8
* 9 = 9
* 10 = 10
* Jack = 11
* Queen = 12
* King = 13
* Ace = 14

> \* Zonder deze regel kan een aas nooit verliezen en blijft deze kaart dus altijd in de stapel van de speler. Met deze regel bestaat die mogelijkheid wel. 

## Analyse

Kijkend naar de spelregels hierboven zijn er eigenlijk drie elementen waarmee het spel gespeeld wordt:

* Een kaart
* Een pak kaarten
* Een stapel kaarten

Dit is wat er in de spelregels gebeurt met ieder element:

* Kaart
    * Bestaan er 52 van, alle normale kaarten in een kaartspel (alle `suit`s en `value`s)
    * Kaarten worden in het spel met elkaar vergeleken op waarde. 
* Een pak kaarten:
    * Word in het begin gehusseld
    * Word in tweeën gedeeld over twee stapels
* Een stapel kaarten:
    * Word de bovenste kaart van gepakt
    * Worden onderaan kaarten toegevoegd
    * Word gekeken hoeveel kaarten er nog in de stapel zitten.

## Classes

In het verlengde van wat ieder element in het spel moet kunnen hebben we de volgende classes ontworpen:

    class Card:
        def __init__(self, suit: str, value: str) -> None:
            """
            Initialize a card with given suit and value.
            """
            self.suit = suit
            self.value = value

        def get_value(self) -> int:
            """
            Returns a value between 2 and 14 (inclusive).
            Where J = 11, Q = 12, K = 13, A = 14
            """
            
        def description(self) -> str:
            """
            Returns a description of the card in the following way:
            value of suit
            """

    class DrawPile:
        def __init__(self) -> None:
            """
            Initialize an empty draw pile.
            """

        def draw_card(self) -> Card | None:
            """
            Draw a card from the top of the pile and remove it from the pile.
            Returns None if there are no cards in the pile.
            """

        def add_card(self, card: Card) -> None:
            """
            Add a card to the bottom of the pile.
            """

        def count_cards(self) -> int:
            """
            Count the number of cards in the pile.
            """

    class Deck:
        def __init__(self) -> None:
            """
            Create a deck of 52 cards.
            """

        def shuffle(self) -> None:
            """
            Shuffle all cards in the deck.
            """

        def deal(self) -> Card | None:
            """
            Deal a single card and remove it from the deck.
            Returns None if there are no cards in the Deck.
            """

        def split_deck(self) -> tuple[DrawPile, DrawPile]:
            """
            Evenly split the deck into two draw piles.
            The deck is empty after splitting.
            """


## Stap 1: Implementeer Card, Deck en DrawPile

Implementeer de classes `Card`, `Deck` en `DrawPile` in een bestand genaamd `war.py`. Je kan de implementatie testen met onderstaande pytest tests.

<details markdown="1"><summary markdown="span">`test_war.py`</summary>

    from war import Card, Deck, DrawPile

    def test_card_description():
        card = Card('Hearts', 'A')
        assert card.description() == 'A of Hearts'

    def test_card_get_value():
        card = Card('Spades', 'K')
        assert card.get_value() == 13

    def test_deck_deal():
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        
        all_combinations: list[tuple[str, str]] = []
        for suit in suits:
            for value in values:
                all_combinations.append((suit, value))
        
        # assert that all 52 cards are dealt
        deck = Deck()
        for _ in range(52):
            dealt_card = deck.deal()

            combination = (dealt_card.suit, dealt_card.value)
            assert combination in all_combinations
            all_combinations.remove(combination)

    def test_deck_split():
        deck = Deck()
        pile1, pile2 = deck.split_deck()
        assert pile1.count_cards() == 26
        assert pile2.count_cards() == 26
        assert deck.deal() == None

    def test_draw_pile_count_cards():
        draw_pile = DrawPile()
        assert draw_pile.count_cards() == 0

        card = Card('Spades', 'Q')
        draw_pile.add_card(card)
        assert draw_pile.count_cards() == 1

    def test_draw_pile_add_card():
        card = Card('Hearts', '9')
        draw_pile = DrawPile()
        draw_pile.add_card(card)
        assert draw_pile.count_cards() == 1

    def test_draw_pile_draw_card():
        card1 = Card('Diamonds', '7')
        card2 = Card('Clubs', '8')
        
        draw_pile = DrawPile()
        draw_pile.add_card(card1)
        draw_pile.add_card(card2)
        
        drawn_card = draw_pile.draw_card()
        assert drawn_card == card1
        assert draw_pile.count_cards() == 1
        
        drawn_card = draw_pile.draw_card()
        assert drawn_card == card2
        assert draw_pile.count_cards() == 0

</details>

Dit zijn alle values:

    ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

Dit zijn alle suits:

    ['Hearts', 'Diamonds', 'Clubs', 'Spades']


## Stap 2: implementeer het spel

Implementeer nu het spel zodat het programma output in de volgende vorm produceert:

    $ python3 war.py
    Round 1:
    Player 1 draws A of Diamonds
    Player 2 draws 2 of Clubs
    Player 1 wins this round!

    Round 2:
    Player 1 draws 3 of Diamonds
    Player 2 draws Q of Diamonds
    Player 2 wins this round!

    Round 3:
    Player 1 draws 10 of Spades
    Player 2 draws 8 of Hearts
    Player 1 wins this round!

    Round 4:
    Player 1 draws Q of Spades
    Player 2 draws 3 of Hearts
    Player 1 wins this round!

    Round 5:
    Player 1 draws 9 of Spades
    Player 2 draws 9 of Diamonds
    It's a tie!

    ...

    Round 171:
    Player 1 draws 9 of Spades
    Player 2 draws 9 of Hearts
    It's a tie!

    Round 172:
    Player 1 draws Q of Clubs
    Player 2 draws 9 of Hearts
    Player 1 wins this round!

    Player 1 wins the game with 52 cards!

> Let op, de output hierboven is ingekort met `...`. Jouw implementatie moet natuurlijk wel alle rondes laten zien.

> Er zit willekeur in het spel, dus ieder spel zal anders lopen.

> Er is geen input nodig van de spelers, het spel loopt automatisch door en eindigt vanzelf.

Bij gelijkspel moet het laatste bericht zijn:

    The game is a tie!

Zijn er meer dan 1000 rondes nodig, dan kan de laatste ronde er zo uit zien:

    Round 1000:
    Player 1 draws 2 of Spades
    Player 2 draws 9 of Clubs
    Player 2 wins this round!

    Player 1 wins the game with 28 cards!