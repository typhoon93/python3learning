"""
Lessons:

1. we can implement a len method for an object, so we can take advantage of the python built in LEN -> then we don't have to memorize and use
arbitrarily created lenth methods for our objects.
2. We can use the __getitem__ method to create a standartized and unique way of accessing data that our collections represent.
    - standartized interface
    - supports slicing
    - deck is iterable
    - can be iterated in reverse
    - can use the "in" operator

3. By implementing the special methods __len__ and __getitem__, our FrenchDeck behaves like a standard Python sequence, 
allowing it to benefit from core language features (e.g., iteration and slicing) and from the standard library, as shown by the
examples using random.choice, reversed, and sorted

4. Python len function gets the lengths of the object directly, if we use it on built in types like list, str, bytearray etc, so it is cost effective.
5. do not call special methods like __len__ directly, just use built in func like len, iter, str; for built in types, they are faster than method calls.


"""

import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    # beer_card = Card("7", "diamonds")
    # print(beer_card)
    deck = FrenchDeck()

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    print(len(deck))
    print(deck[0])
    print(deck[-1])
    print(choice(deck))
    print(deck[12::13])  # slicing to just get the aces
    print(Card("Q", "hearts") in deck)

    for card in sorted(deck, key=spades_high):
        print(card)
