from modules.game_model_mod import GameModel


class GameController:
    def __init__(self, model: GameModel) -> None:
        self.model = model

    def set_view(self, view):
        self.view = view

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
        self.model.add_card_to_slot(slot_id, card_value)

    # def start_game(self):
    #     while True:
    #         card_value = self.model.draw_a_card()
    #         self.view.show_slots(self.model.get_slots())
    #         self.view.show_drawn_card(card_value[0])

    #         withdraw = False
    #         if self.model.withdraw_condition():
    #             withdraw = True

    #         will_be_busted = self.model.check_will_be_busted(card_value[1])

    #         if withdraw and will_be_busted:
    #             print(f"WIN {self.get_winning_value()}")
    #             break
    #         elif will_be_busted:
    #             print("BUSTED!")
    #             break

    #         # ASK FOR THE USER INPUT
    #         slot_id = self.view.ask_for_the_slot(withdraw)

    #         if slot_id is None:
    #             print(f"WIN {self.get_winning_value()}")
    #             break

    #         if not self.model.add_card_to_slot(slot_id, card_value[1]):
    #             self.view.show_slots(self.model.get_slots())
    #             print("BUSTED")
    #             break

    #         if self.model.get_total() == 105:
    #             self.view.show_slots(self.model.get_slots())
    #             print(f"WIN {self.get_winning_value()}")
    #             break
