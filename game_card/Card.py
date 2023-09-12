# The class Card includes data(value and unit) about the card and the following Methods:
# __str__
# __gt__
# __eq__

class Card:
    def __init__(self, value, suit):
        """Defines new card: value and suit"""
        self.value = value
        if self.value < 1 or self.value > 13:
            raise ValueError("Value must be between 1-13")
        self.suit = suit
        if self.suit < 1 or self.suit > 4:
            raise ValueError("Suit must be between 1-4")

    def __repr__(self):
        list_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        list_suits = ['Diamond', 'Spade', 'Heart', 'Club']
        return (f'{list_values[self.value - 1]} of {list_suits[self.suit - 1]}')

    def __gt__(self, other):
        """Checks if the card higher than other card"""
        if type(other) != Card:
            raise TypeError("Other must be a Card")
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            elif self.suit < other.suit:
                return False
        else:
            if self.value == 1:
                return True
            else:
                if other.value == 1:
                    return False
                else:
                    if self.value > other.value:
                        return True
                    else:
                        return False

    def __eq__(self, other):
        """Compares between 2 cards"""
        if type(other) != Card:
            raise TypeError("Other must be a Card")
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False
