from random import seed
from datetime import datetime
import random

from modules.card_slot_mod import CardSlot


class GameModel:
    """
    This represent the Game Model
    """

    cards = [
        ("A", 11),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
        ("10", 10),
        ("J", 10),
        ("Q", 10),
        ("K", 10),
    ]

    def __init__(self) -> None:
        """
        Initialize the model
        """
        self.restart()

    def restart(self):
        self._slots = (
            CardSlot(0),
            CardSlot(1),
            CardSlot(2),
            CardSlot(3),
            CardSlot(4),
        )

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
            total += slot.shown_value
        return total

    def a_slot_is_flashing(self) -> bool:
        """
        Check if there is at least a slot flashing
        """
        for slot in self._slots:
            if slot.flashing:
                return True
        return False

    def is_busted(self):
        """
        Check if there is at least a slot busted
        """
        for slot in self._slots:
            if slot.is_busted:
                return True
        return False

    def draw_a_card(self):
        """
        Return a random value from 1 to 11
        """
        seed(datetime.now().timestamp())
        return random.choice(GameModel.cards)

    def check_will_be_busted(self, card_value) -> bool:
        """
        Check if the game is in a sure busted condition
        """
        if card_value == 11:
            card_value = 1
        if self.a_slot_is_flashing():
            return False
        for slot in self._slots:
            if slot.real_value + card_value <= 21:
                return False
        return True

    def withdraw_condition(self) -> bool:
        """
        Check if is possible withdraw something
        """
        total = self.get_total()
        if 100 <= total <= 105:
            return True
        return False
