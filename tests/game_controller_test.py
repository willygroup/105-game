import unittest

from modules.game_controller_mod import GameController
from unittest.mock import MagicMock

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
    def set_shown_values_in_model(model, values):
        for index, value in enumerate(values):
            model._slots[index].shown_value = value

    def set_up_game_controller(self):
        model = GameModel()
        view = None
        # model.get_total = MagicMock(return )
        return GameController(model, view)

    def test_get_winning_value(self):
        for values, expected_winning in test_winning_value_cases:
            with self.subTest():
                controller = self.set_up_game_controller()
                controller.model.get_total = MagicMock(return_value=values)

                self.assertEqual(controller.get_winning_value(), expected_winning)


if __name__ == "__main__":
    unittest.main()
