from random import seed
from random import randint
from datetime import datetime

from modules.slots_mod import Slots


class GameModel:
    """
    This represent the whole Game
    """

    def __init__(self) -> None:
        self._slots = Slots()

    def get_total(self) -> int:
        return self._slots.get_total()

    def a_slot_is_flashing(self) -> bool:
        return self._slots.is_flashing()

    # TODO
    def is_busted():
        pass

    def get_slots(self):
        return self._slots.get_slots()

    def add_card_to_slot(self, id, card_value):
        return self._slots.add_card_to_slot(id, card_value)

    # TODO
    @staticmethod
    def draw_a_card():
        """
        Return a random value from 1 to 11
        """
        seed(datetime.now().timestamp())
        return randint(2, 11)
