class GameView:
    def __init__(self) -> None:
        pass

    def set_controller(self, controller):
        self._controller = controller

    def show_slots(self, slots):
        slot_txt = ""
        total = 0
        for slot in slots:
            suffix = ""
            if slot.flashing:
                suffix = "*"
            elif slot.is_busted():
                suffix = "#"
            slot_txt += f"[{slot.shown_value}{suffix}]"
            if slot.id != len(slots) - 1:
                slot_txt += " "
            total += slot.shown_value
        print(f"{slot_txt} - Total: {total}")

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
