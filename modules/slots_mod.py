from modules.card_slot_mod import CardSlot


class Slots:
    """
    This represent the whole set of CardSlot
    """

    def __init__(self) -> None:
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
            total += slot.showed_value
        return total

    def is_flashing(self) -> bool:
        for slot in self._slots:
            if slot.flashing:
                return True
        return False
