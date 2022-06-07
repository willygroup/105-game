from random import seed
from random import randint
from datetime import datetime

from modules.card_slot_mod import CardSlot


class GameModel:
    """
    This represent the whole Game
    """

    def __init__(self) -> None:
        self._slots = (
            CardSlot(0),
            CardSlot(1),
            CardSlot(2),
            CardSlot(3),
            CardSlot(4),
        )

    # try to add
    # Fixme
    def check_will_be_busted(self, card_value) -> bool:
        if card_value == 11:
            card_value = 1
        if self.a_slot_is_flashing():
            return False
        for slot in self._slots:
            if slot.showed_value + card_value <= 21:
                return False
        return True

    def withdraw_condition(self) -> bool:
        total = self.get_total()
        if 100 <= total <= 105:
            return True
        return False

    def add_card_to_slot(self, slot_id: int, card_value: int) -> bool:
        """
        Add a card_value to a slot and return the `busted` status
        """
        return self._slots[slot_id].add_card(card_value)

    def get_slots(self):
        return self._slots

    def get_total(self) -> int:
        """
        Get the total value
        """
        total = 0
        for slot in self._slots:
            total += slot.showed_value
        return total

    def a_slot_is_flashing(self) -> bool:
        for slot in self._slots:
            if slot.flashing:
                return True
        return False

    def is_busted(self):
        for slot in self._slots:
            if slot.is_busted:
                return True
        return False

    @staticmethod
    def draw_a_card():
        """
        Return a random value from 1 to 11
        """
        seed(datetime.now().timestamp())
        return randint(2, 11)
