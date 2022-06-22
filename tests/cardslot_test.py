import unittest
import os


from modules.card_slot_mod import CardSlot

from unittest import TestCase

bad_args_list = [
    (None, TypeError),
    ("", TypeError),
    ("3", TypeError),
    (-1, TypeError),
    (6, TypeError),
]

good_args_list = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
]

# (shown_value, real_value, n_cards, flashing, busted),<card>, expected_values
add_card_list = [
    ((3, 3, 1, False, False), 5, (8, 8, 2, False, False)),
    ((3, 3, 1, False, False), 11, (14, 14, 2, True, False)),
    ((20, 20, 4, False, False), 3, (23, 23, 5, False, True)),
    ((21, 16, 5, False, False), 3, (21, 19, 6, False, False)),
    ((21, 16, 5, True, False), 7, (21, 13, 6, False, False)),
    ((21, 21, 3, False, False), 7, (28, 28, 4, False, True)),
    ((10, 10, 1, False, False), 11, (21, 21, 2, True, False)),
    ((0, 0, 0, False, False), 11, (11, 11, 1, True, False)),
    ((13, 13, 2, True, False), 11, (14, 14, 3, False, False)),
    ((20, 20, 3, False, False), 11, (21, 21, 4, False, False)),
    ((11, 11, 3, False, False), 11, (12, 12, 4, False, False)),
    ((11, 11, 1, True, False), 11, (12, 12, 2, True, False)),
]


class CardBoxModule(TestCase):
    def create_empty_card_slot(self):
        return CardSlot(0)

    def create_busted_card_slot(self):
        card_slot = CardSlot(0)
        card_slot.shown_value = 22
        card_slot.real_value = 22
        card_slot.n_cards = 4
        card_slot.flashing = False
        card_slot.busted = True
        return card_slot

    def get_dirname(self) -> str:
        dirname = os.path.realpath(__file__)
        dirname = os.path.split(dirname)[0]
        return dirname

    def test_init_with_bad_args(self):
        for input, expected in bad_args_list:
            with self.subTest():
                with self.assertRaises(expected):
                    CardSlot(input)

    def test_init_example_with_args(self):
        for input, expected in good_args_list:
            with self.subTest():
                card = CardSlot(input)
                self.assertEqual(card.id, expected)

    def test_add_card(self):
        for input, card_value, expected in add_card_list:
            with self.subTest():
                card = CardSlot(0)

                card.shown_value = input[0]
                card.real_value = input[1]
                card.n_cards = input[2]
                card.flashing = input[3]
                card.busted = input[4]

                res = card.add_card(card_value)

                self.assertEqual(card.shown_value, expected[0])
                self.assertEqual(card.real_value, expected[1])
                self.assertEqual(card.n_cards, expected[2])
                self.assertEqual(card.flashing, expected[3])
                self.assertEqual(card.busted, expected[4])
                self.assertEqual(res, expected[4])

    def test_is_busted(self):
        card_slot = self.create_busted_card_slot()

        self.assertTrue(card_slot.is_busted())


if __name__ == "__main__":
    unittest.main()
