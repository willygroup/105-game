from modules.game_model_mod import GameModel
from modules.game_view_mod import GameView


class GameController:
    def __init__(self, model: GameModel, view: GameView) -> None:
        self.model = model
        self.view = view

    def start_game(self):
        while True:
            partial_total: int = self.model.get_total()
            card_value = self.model.draw_a_card()
            self.view.show_slots(self.model.get_slots())
            self.view.show_drawn_card(card_value)

            temp_card_value = card_value
            if card_value == 11:
                temp_card_value = 1

            # TODO add this check on controller, then call
            # self.controller.bust_check(card_value)
            # self.controller.withdraw_condition()
            # ...
            if (
                not self.model.a_slot_is_flashing()
                and partial_total < 100
                and partial_total + temp_card_value > 105
            ):
                print("BUSTED")
                break

            # ASK FOR THE USER INPUT
            slot_id = self.view.ask_for_the_slot()
            if not self.model.add_card_to_slot(slot_id, card_value):
                self.view.show_slots(self.model.get_slots())
                print("BUSTED")
                break
