from Card import Card
from unittest import TestCase


class test_Card(TestCase):
    def setUp(self):
        self.card1 = Card(13, 4)
        self.card2 = Card(1, 1)

    def test_init_valid(self):
        """Test case: valid input"""
        self.assertEqual(13, self.card1.value)
        self.assertEqual(4, self.card1.suit)
        self.assertEqual(1, self.card2.value)
        self.assertEqual(1, self.card2.suit)

    def test_init_invalid(self):
        """Test case: invalid input"""
        with self.assertRaises(ValueError):
            card = Card(0, 3)
        with self.assertRaises(ValueError):
            card = Card(14, 3)
        with self.assertRaises(ValueError):
            card = Card(7, 0)
        with self.assertRaises(ValueError):
            card = Card(7, 5)

    def test_gt_valid(self):
        """Test case valid inputs"""
        # Test case with Ace
        self.assertFalse(self.card1 > self.card2)
        # Test case same Value: 8 of diamond VS 8 of heart
        self.assertTrue(Card(8, 3) > Card(8, 1))
        # Test case same suit: 9 of diamond VS 8 of diamond
        self.assertTrue(Card(9, 3) > Card(8, 3))
        # Test case same Value(Ace): Ace of diamond VS Ace of heart
        self.assertTrue(Card(1, 3) > Card(1, 1))
        # Test case same Value and suit: 8 of diamond VS 8 of diamond
        #self.assertn(Card(8, 3) > Card(8, 3))

    def test_gt_invalid(self):
        """Test case invalid: comparing between Card and NOT Card"""
        with self.assertRaises(TypeError):
            Card(5, 3).__gt__('card')

    def test_eq_valid(self):
        """Test case valid inputs"""
        # Test same Values: True
        self.assertTrue(Card(7, 3) == Card(7, 2))
        # Test same Suits: False
        self.assertFalse(Card(5, 3) == Card(7, 3))

    def test_eq_invalid(self):
        """Test case invalid: comparing between Card and NOT Card"""
        with self.assertRaises(TypeError):
            Card(5, 3).__eq__('card')


