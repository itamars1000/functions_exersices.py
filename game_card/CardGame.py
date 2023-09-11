from DeckOfCard import DeckOfCards
from Player import Player
# The class CardGame includes data about the game and the following Methods:
# new_game
# get_winner
# __str__


class CardGame:
    def __init__(self, cards_deck: DeckOfCards, player1: Player, player2: Player):
        """This method define new game with 2 players and start him"""
        self.cards_deck = cards_deck
        self.player1 = player1
        self.player2 = player2
        self.new_game()

    def __str__(self):
        pass

    def new_game(self):
        """Define new game, shuffles the cards and divides cards"""
        if __name__ == "__init__":
            self.cards_deck.cards_shuffle()
            self.player1.set_hand()
            self.player2.set_hand()

    def get_winner(self):
        """This method return the winner who is the player with more cards"""
        if len(self.player1.list_cards) > len(self.player2.list_cards):
            return self.player1
        elif len(self.player1.list_cards) < len(self.player2.list_cards):
            return self.player2
        else:
            return None
