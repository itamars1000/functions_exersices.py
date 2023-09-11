# The class Card includes data(value and unit) about the card and the following Methods:
# __str__
# __gt__
# __eq__

class Card:
    def __init__(self, value, suit):
        """Defines new card: value and suit"""
        self.value = value
        self.suit = suit

    def __repr__(self):
        list_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        list_suits = ['Diamond', 'Spade', 'Heart', 'Club']
        return (f'{list_values[self.value - 1]} of {list_suits[self.suit - 1]}')

    def __gt__(self, other):
        """Checks if the card higher than other card"""
        if self == other:
            if self.suit > other.suit:
                return True
            elif self.suit < other.suit:
                return False
            else:
                return None
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
        if self.value == other.value:
            return True
        else:
            return False
