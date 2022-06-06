import unittest
import os

# pylint: disable=import-error
from commons import prepare_env, restore_env

# pylint: disable=import-error
from modules.slots_mod import Slots


class TestSlotsModule(unittest.TestCase):
    def get_dirname(self) -> str:
        dirname = os.path.realpath(__file__)
        dirname = os.path.split(dirname)[0]
        return dirname

    def test_init_example_without_args(self):

        slots = Slots()

        self.assertEqual(slots._slots[0].id, 0)
        self.assertEqual(slots._slots[1].id, 1)
        self.assertEqual(slots._slots[2].id, 2)
        self.assertEqual(slots._slots[3].id, 3)
        self.assertEqual(slots._slots[4].id, 4)

    # TODO add more cases
    def test_add_card_to_slot(self):
        slots = Slots()
        res = slots.add_card_to_slot(3, 11)

        self.assertTrue(res)
        self.assertEqual(slots.get_total(), 11)


if __name__ == "__main__":
    unittest.main()
