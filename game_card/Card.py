# The class Card includes data(value and unit) about the card and the following Methods:
# __str__
# __gt__
# __eq__

class Card:
    def __init__(self, value, suit):
        """Defines new card: value and suit"""
        self.value = value
        self.suit = suit

    def __str__(self):
        return (f'"Value: {self.value}\n'
                f'Suit: {self.suit}')

    def __gt__(self, other):
        """Checks if the card higher than other card"""
        if self.value > other.value:
            return True
        else:
            return False

    def __eq__(self, other):
        """Compares between 2 cards"""
        if self.value == other.value:
            return True
        else:
            return False
