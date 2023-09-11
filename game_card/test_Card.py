from Card import Card
from unittest import TestCase


class test_Card(TestCase):
    def setUp(self):
        self.card = Card(5, 3)

    def test_init_valid(self):
        """Test case: valid input"""
        self.assertEqual(5, self.card.value)
        self.assertEqual(3, self.card.suit)
