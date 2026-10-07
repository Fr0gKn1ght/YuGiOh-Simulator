import unittest
from board import Board
from card import Card, MonsterCard, SpellCard, TrapCard

class TestBoard(unittest.TestCase):
    def test_get_card(self):
        game_board = Board()
        card = MonsterCard("Test Monster", 3, 200, 200, [])
        game_board.field["p1"]["f1"] = card
        self.assertEqual(game_board.get_card("p1", "f1"), card)

    def test_set_card(self):
        game_board = Board()
        my_card = MonsterCard("Test Monster", 3, 200, 200, [])
        game_board.place_card(my_card, "p1", "f1")
        self.assertEqual(game_board.field["p1"]["f1"], my_card)
        