from DeckOfCard import DeckOfCards
from unittest import TestCase
from Card import Card
from random import randint


class test_deckOfCards(TestCase):
    def setUp(self):
        pass
        self.deck = DeckOfCards()

    def test_init_valid(self):
        """Test valid cases"""
        # check if the cards deck is list
        self.assertEqual(list, type(self.deck.cards))
        # check if in the deck exist 52 cards
        self.assertEqual(52, len(self.deck.cards))
        # check if all the cards is from Card type
        self.assertEqual(Card, type(self.deck.cards[randint(1, 52)]))

    def test_cards_shuffle(self):
        """Test if the deck is still with 52 cards"""
        print(self.deck.cards)
        self.deck.cards_shuffle()
        print(self.deck.cards)
        self.assertEqual(52, len(self.deck.cards))

    def test_deal_one(self):
        """Test if one card is down from the deck"""
        self.deck.deal_one()
        self.assertEqual(51, len(self.deck.cards))
