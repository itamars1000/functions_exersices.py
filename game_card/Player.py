from DeckOfCard import DeckOfCards
from random import choice
from Card import Card


# The class Player includes data(name, number of card,list of cards) about the cards deck and the following Methods:
# set_hand
# get_card
# add_card


class Player:
    def __init__(self, name, numb_cards=26):
        """define the name player and number of cards and the list of cards"""
        self.name = name
        if type(self.name) != str:
            raise TypeError("name must be string ")
        self.numb_cards = numb_cards
        if self.numb_cards < 0:
            raise ValueError("value must be positive ")
        if self.numb_cards > 26 or self.numb_cards < 10:
            self.numb_cards = 26
        self.list_cards = []

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return (f'Name: {self.name}\n'
                f'Cards: {self.list_cards}')

    def set_hand(self, cards_deck: DeckOfCards):
        """function divide random cards to the player"""
        for i in range(self.numb_cards):
            card = cards_deck.deal_one()
            self.add_card(card)

    def get_card(self):
        """choose random card from the list of cards"""
        if self.list_cards == []:
            raise Exception("The player finished his cards")
        card = choice(self.list_cards)
        self.list_cards.remove(card)
        return card

    def add_card(self, card: Card):
        """function will get a card and will add it to the list of cards"""
        self.list_cards.append(card)
