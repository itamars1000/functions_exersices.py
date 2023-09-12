from  CardGame import CardGame
from unittest import TestCase
from Player import Player
from DeckOfCard import DeckOfCards
from unittest import mock
from unittest.mock import patch
from Card import Card
from DeckOfCard import DeckOfCards


class test_cardGame(TestCase):
    def setUp(self):
        self.my_game = CardGame(DeckOfCards(), Player('AAA'), Player('BBB'))

    def test_init_valid(self):
        """Test case valid inputs"""
        deck = DeckOfCards()
        my_player1 = Player('aaa')
        my_player2 = Player('bbb')
        game = CardGame(deck, my_player1, my_player2)
        self.assertEqual(deck, game.cards_deck)
        self.assertEqual(my_player1, game.player1)
        self.assertEqual(my_player2, game.player2)

    def test_init_invalid1(self):
        """Test case invalid input: deck"""
        with self.assertRaises(TypeError):
            deck = [2, 3, 5, 7, 8]
            my_player1 = Player('aaa')
            my_player2 = Player('bbb')
            game = CardGame(deck, my_player1, my_player2)

    def test_init_invalid2(self):
        """Test case invalid input: player1"""
        with self.assertRaises(TypeError):
            deck = DeckOfCards()
            my_player1 = 'Player'
            my_player2 = Player('bbb')
            game = CardGame(deck, my_player1, my_player2)

    def test_init_invalid3(self):
        """Test case invalid input: player2"""
        with self.assertRaises(TypeError):
            deck = DeckOfCards()
            my_player1 = Player('aaa')
            my_player2 = 'Player'
            game = CardGame(deck, my_player1, my_player2)


    def test_new_game_valid1(self):
        """Check if left in the deck right amount of cards after the division"""
        deck1 = DeckOfCards()
        game1 = CardGame(deck1, Player('aaa', 20), Player('BBB', 20))
        self.assertEqual(12, len(deck1.cards))

    def test_new_game_valid2(self):
        """Test case that check if the players get the right amount of cards"""
        deck1 = DeckOfCards()
        player1 = Player('aaa', 10)
        player2 = Player('bbb', 10)
        game1 = CardGame(deck1, player1, player2)
        self.assertEqual(10, len(player1.list_cards))
        self.assertEqual(10, len(player2.list_cards))

    def test_new_game_invalid(self):
        """Test case that check if the program stops if there is try to start new game"""
        with self.assertRaises(Exception):
            self.my_game.new_game()

    def test_get_winner_valid1(self):
        """Check if player1 with more cards is winning"""
        self.my_game.player1.numb_cards = 23
        self.my_game.player1.set_hand(DeckOfCards())
        self.my_game.player2.numb_cards = 22
        self.my_game.player2.set_hand(DeckOfCards())
        self.assertEqual(self.my_game.player1, self.my_game.get_winner())

    def test_get_winner_valid2(self):
        """Check if player2 with more cards is winning"""
        self.my_game.player1.numb_cards = 23
        self.my_game.player1.set_hand(DeckOfCards())
        self.my_game.player2.numb_cards = 24
        self.my_game.player2.set_hand(DeckOfCards())
        self.assertEqual(self.my_game.player2, self.my_game.get_winner())

    def test_get_winner_valid3(self):
        """Check if return NONE if there is even"""
        self.my_game.player1.numb_cards = 22
        self.my_game.player1.set_hand(DeckOfCards())
        self.my_game.player2.numb_cards = 22
        self.my_game.player2.set_hand(DeckOfCards())
        self.assertEqual(None, self.my_game.get_winner())


