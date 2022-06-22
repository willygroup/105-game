import unittest
from modules.card_slot_mod import CardSlot

from modules.game_controller_mod import GameController
from unittest.mock import MagicMock
from unittest.mock import Mock

from modules.game_model_mod import GameModel

test_winning_value_cases = [
    [54, None],
    [0, None],
    [105, 10],
    [99, None],
    [104, 8],
    [100, 1],
    [103, 1],
]


class GameControllerModule(unittest.TestCase):
    @staticmethod
    def create_game_controller():

        model = Mock()

        card_slot_3 = CardSlot(3)
        card_slot_3.shown_value = 15
        card_slot_3.n_cards = 3
        card_slot_3.real_value = 15
        card_slot_3.flashing = True

        model.get_slots.return_value = (
            CardSlot(0),
            CardSlot(1),
            CardSlot(2),
            card_slot_3,
            CardSlot(4),
        )

        return GameController(model)

    @staticmethod
    def set_shown_values_in_model(model, values):
        for index, value in enumerate(values):
            model._slots[index].shown_value = value

    def set_up_game_controller(self):
        model = GameModel()
        # model.get_total = MagicMock(return )
        return GameController(model)

    def test_get_winning_value(self):
        for values, expected_winning in test_winning_value_cases:
            with self.subTest():
                controller = self.set_up_game_controller()
                controller.model.get_total = MagicMock(return_value=values)

                self.assertEqual(controller.get_winning_value(), expected_winning)

    def test_get_slot_values(self):
        controller = self.create_game_controller()
        slot = controller.get_slot_values(3)
        self.assertEqual(slot[0], 15)
        self.assertEqual(slot[1], 15)
        self.assertEqual(slot[2], 3)
        self.assertEqual(slot[3], True)
        self.assertEqual(slot[4], False)


if __name__ == "__main__":
    unittest.main()
