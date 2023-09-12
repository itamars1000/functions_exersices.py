from Player import Player
from Card import Card
from unittest import TestCase
from unittest import mock
from unittest.mock import patch
from DeckOfCard import DeckOfCards
class test_player(TestCase):
    def test_set_hand(self):
        assert False

    def test_get_card_valid(self):
        """Check if the card not in the player cards"""
        my_player = Player('aaa', 10)
        my_player.set_hand(DeckOfCards())
        my_player.get_card()
        self.assertEqual(9, len(my_player.list_cards))
        self.assertNotIn(my_player.get_card(), my_player.list_cards)


    def test_add_card(self):
        assert False
