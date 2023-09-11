from CardGame import CardGame
from Player import Player
from DeckOfCard import DeckOfCards

# Divides cards to players
deck1 = DeckOfCards()
print("New player")
player1 = Player(input("name:"), 26)
player1.set_hand(deck1)
print("New player")
player2 = Player(input("name:"), 26)
player2.set_hand(deck1)
print(player1.__repr__())
print(player2.__repr__())

# SetUp game
game = CardGame(deck1, player1, player2)

# Play 10 rounds
input("")
for i in range(10):
    card1 = player1.get_card() # Player1 gets a card
    print(card1)
    card2 = player2.get_card() # Player2 gets a card
    print(card2)

    # Checking who won

    if card1 == card2:
        if card1.suit > card2.suit:
            player1.add_card(card1)
            player1.add_card(card2)
            print(player1.__str__())
        elif card2.suit > card1.suit:
            player2.add_card(card1)
            player2.add_card(card2)
            print(player2.__str__())
        else:
            player1.add_card(card1)
            player2.add_card(card2)
            print("Even")
    else:
        if card1 > card2:
            player1.add_card(card1)
            player1.add_card(card2)
            print(player1.__str__())
        else:
            player2.add_card(card1)
            player2.add_card(card2)
            print(player2.__str__())
    input("")

# The results
print(f'The winner of the game is {game.get_winner()}')

