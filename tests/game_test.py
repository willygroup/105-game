import unittest


# pylint: disable=import-error
from modules.game_model_mod import GameModel


class TestGameModule(unittest.TestCase):
    def test_init_game(self):
        GameModel()

    def test_draw_a_card(self):
        for _ in range(0, 100):
            self.assertTrue(
                GameModel.draw_a_card() in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
            )  #


if __name__ == "__main__":
    unittest.main()
