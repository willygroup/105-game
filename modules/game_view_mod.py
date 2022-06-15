# DELETEME


class GameView:
    def __init__(self) -> None:
        pass

    def set_controller(self, controller):
        self._controller = controller

    def show_slots(self, slots):
        slot_txt = ""
        real_values = ""
        n_cards_text = ""
        total = 0
        for slot in slots:
            suffix = " "
            if slot.flashing:
                suffix = "*"
            elif slot.is_busted():
                suffix = "#"
            slot_txt += f"[ {slot.shown_value:2d}{suffix}]"
            real_values += f"[ {slot.real_value:2d}{suffix}]"
            n_cards_text += f"[ {slot.n_cards:2d} ]"
            if slot.id != len(slots) - 1:
                slot_txt += " "
                real_values += " "
                n_cards_text += " "
            total += slot.shown_value
        print(f"{slot_txt} - Total: {total}\n{real_values}\n{n_cards_text}")

    def show_drawn_card(self, card_value):
        print(f">>> {card_value} <<<")

    def ask_for_the_slot(self, withdraw) -> int:

        text = "Please enter the slot [1, 5] "
        if withdraw:
            text += "\nType X to withdraw thw winning: "
        else:
            text += ": "

        var = 0
        while var not in range(1, 6) and var != "X":
            var = input(text)
            if var != "X":
                try:
                    var = int(var)
                except Exception:
                    var = 0
            else:
                return None

        return var - 1
