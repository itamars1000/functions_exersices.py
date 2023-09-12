from Card import Card
from random import shuffle, choice

# The class DeckOfCards includes data about the cards deck and the following Methods:
# cards_shuffle
# deal_one
# __repr__


class DeckOfCards:
    def __init__(self):
        """Make new deck of card with 52 cards"""
        self.cards = [Card(i, j) for i in range(1, 14) for j in range(1, 5)]

    def __repr__(self):
        return f'Deck of cards: {self.cards}'

    def cards_shuffle(self):
        """Shuffle the cards deck"""
        shuffle(self.cards)

    def deal_one(self):
        """Pick one card from the deck and take it"""
        card = choice(self.cards)
        self.cards.remove(card)
        return card
