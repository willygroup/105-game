from typing import Tuple
from modules.game_model_mod import GameModel


class GameController:
    def __init__(self, model: GameModel) -> None:
        self.model = model

    def set_view(self, view):
        self.view = view

    def restart(self):
        self.model.restart()

    def get_total(self) -> int:
        return self.model.get_total()

    def check_will_be_busted(self, card_value) -> bool:
        return self.model.check_will_be_busted(card_value)

    def get_winning_value(self):
        total = self.model.get_total()
        if total == 105:
            return 10
        elif total == 104:
            return 8
        elif 99 < total < 104:
            return 1
        return None

    def add_card_to_slot(self, slot_id, card_value) -> bool:
        return self.model.add_card_to_slot(slot_id, card_value)

    def get_slot_values(self, slot_id) -> Tuple:
        slot = self.model.get_slots()[slot_id]
        return (
            slot.shown_value,
            slot.real_value,
            slot.n_cards,
            slot.flashing,
            slot.is_busted(),
        )
