from Player import Player
from Card import Card
from unittest import TestCase
from unittest import mock
from unittest.mock import patch
from DeckOfCard import DeckOfCards


class test_player(TestCase):
    def setUp(self):
        self.player1 = Player("dani", 24)

    def test_init_valid(self):
        """test cases: valid cases for init """
        self.assertEqual("dani",self.player1.name)
        self.assertEqual(24,self.player1.numb_cards)
        self.assertEqual([],self.player1.list_cards)
        player2 = Player("dani", 27)
        self.assertEqual(26,player2.numb_cards)
        player3 = Player("dani", 9)
        self.assertEqual(26,player3.numb_cards)

    def test_init_invalid(self):
        """test cases : invalid cases for init """
        with self.assertRaises(TypeError):
            player2=Player(222, 22)
        with self.assertRaises(ValueError):
            player3 = Player('aaa', -1)

    @mock.patch('DeckOfCard.DeckOfCards.deal_one', return_value=Card(3, 3))
    def test_set_hand_valid(self, mock_card):
        """Check if specific card been given to the player"""
        card = Card(3, 3)
        my_player = Player('aaa', 10)
        deck = DeckOfCards()
        my_player.set_hand(deck)
        self.assertIn(card, my_player.list_cards)

    def test_set_hand_invalid(self):
        """Invalid case: Deck is empty"""
        with self.assertRaises(Exception):
            my_player = Player('aaa', 10)
            deck = DeckOfCards()
            deck = [] # The deck is empty
            my_player.set_hand(deck)

    def test_get_card_valid(self):
        """Check if the card not in the player cards"""
        my_player = Player('aaa', 10)
        my_player.set_hand(DeckOfCards())
        my_player.get_card()
        self.assertEqual(9, len(my_player.list_cards))
        self.assertNotIn(my_player.get_card(), my_player.list_cards)

    def test_get_card_invalid(self):
        """Check if the player has still cards"""
        with self.assertRaises(Exception):
            my_player = Player('aaa', 10)
            my_player.list_cards = []
            my_player.get_card()

    def test_add_card_valid(self):
        my_player = Player('aaa', 10)
        my_player.set_hand(DeckOfCards())
        card = Card(2, 2)
        my_player.add_card(card)
        self.assertIn(card, my_player.list_cards)
