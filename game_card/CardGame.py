from DeckOfCard import DeckOfCards
from Player import Player
# The class CardGame includes data about the game and the following Methods:
# new_game
# get_winner
# __str__


class CardGame:
    def __init__(self, cards_deck: DeckOfCards, player1: Player, player2: Player):
        """This method define new game with 2 players and start him"""
        if type(cards_deck) != DeckOfCards:
            raise TypeError("Deck must be DeckOfCards type")
        self.cards_deck = cards_deck
        if type(player1) != Player:
            raise TypeError("player1 must be Player type")
        self.player1 = player1
        if type(player2) != Player:
            raise TypeError("player2 must be Player type")
        self.player2 = player2
        self.new_game()

    def __str__(self):
        pass

    def new_game(self):
        """Define new game, shuffles the cards and divides cards"""
        if len(self.cards_deck.cards) != 52:
            raise Exception("The game already begin")
        self.cards_deck.cards_shuffle()
        self.player1.set_hand(self.cards_deck)
        self.player2.set_hand(self.cards_deck)

    def get_winner(self):
        """This method return the winner who is the player with more cards"""
        if len(self.player1.list_cards) > len(self.player2.list_cards):
            return self.player1
        elif len(self.player1.list_cards) < len(self.player2.list_cards):
            return self.player2
        else:
            return None
