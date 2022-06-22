import unittest

from modules.game_model_mod import GameModel


test_will_be_busted = [
    [(10, 11, 21, 20, 5), 10, False],
    [(0, 0, 0, 0, 0), 11, False],
    [(12, 12, 12, 12, 12), 10, True],
    [(21, 21, 21, 21, 20), 11, False],
    [(21, 21, 21, 21, 20), 5, True],
]

test_withdraw_total_cases = [
    [(10, 11, 21, 30, 5), 77, False],
    [(0, 0, 0, 0, 0), 0, False],
    [(21, 21, 21, 21, 21), 105, True],
    [(11, 10, 10, 10, 10), 51, False],
    [(21, 21, 20, 21, 21), 104, True],
    [(21, 21, 18, 21, 21), 102, True],
]

test_flashing_slots_cases = [
    [(True, False, False, False, False), True],
    [(False, False, False, False, False), False],
    [(False, False, False, True, False), True],
    [(False, False, True, False, False), True],
    [(False, True, False, False, True), True],
]

test_busted_slots_cases = [
    [(True, False, False, False, False), True],
    [(False, False, False, False, False), False],
    [(False, False, False, True, False), True],
    [(False, False, True, False, False), True],
    [(False, True, False, False, False), True],
]


class GameModelModule(unittest.TestCase):
    @staticmethod
    def set_real_values_in_model(model, values):
        for index, value in enumerate(values):
            model._slots[index].real_value = value

    @staticmethod
    def set_shown_values_in_model(model, values):
        for index, value in enumerate(values):
            model._slots[index].shown_value = value

    @staticmethod
    def set_flashing_in_model(model, values):
        for index, value in enumerate(values):
            model._slots[index].flashing = value

    @staticmethod
    def set_busted_in_model(model, values):
        for index, value in enumerate(values):
            model._slots[index].is_busted = value

    def test_get_total(self):
        for values, expected_total, _ in test_withdraw_total_cases:
            with self.subTest():
                model = GameModel()
                self.set_shown_values_in_model(model, values)

                self.assertEqual(model.get_total(), expected_total)

    def test_a_slot_is_flashing(self):
        for values, expected_flashing in test_flashing_slots_cases:
            with self.subTest():
                model = GameModel()
                self.set_flashing_in_model(model, values)

                self.assertEqual(model.a_slot_is_flashing(), expected_flashing)

    def test_is_busted(self):
        for values, expected_busted in test_busted_slots_cases:
            with self.subTest():
                model = GameModel()
                self.set_busted_in_model(model, values)

                self.assertEqual(model.is_busted(), expected_busted)

    def test_will_be_busted(self):
        for values, card_value, expected_busted in test_will_be_busted:
            with self.subTest():
                model = GameModel()
                self.set_real_values_in_model(model, values)

                self.assertEqual(
                    model.check_will_be_busted(card_value), expected_busted
                )

    def test_check_withdraw_condition(self):
        for values, _, withdraw_cond in test_withdraw_total_cases:
            with self.subTest():
                model = GameModel()
                self.set_shown_values_in_model(model, values)

                self.assertEqual(model.withdraw_condition(), withdraw_cond)

    def test_draw_a_card(self):
        for _ in range(0, 1000):
            self.assertTrue(GameModel.draw_a_card() in GameModel.cards)  #


if __name__ == "__main__":
    unittest.main()
