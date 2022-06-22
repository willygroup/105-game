from enum import Enum
from rich import console
from textual.app import App
from textual.views import GridView
from rich.text import Text
from textual.widgets import Button, Static, ButtonPressed
from pyfiglet import Figlet
from textual.reactive import Reactive
from rich.console import RenderableType

from modules.game_controller_mod import GameController
from modules.sounds_mod import Sounds


class FigletText:
    """A renderable to generate figlet text that adapts to fit the container."""

    def __init__(self, text: str) -> None:
        self.text = text

    def __rich_console__(
        self, console: console.Console, options: console.ConsoleOptions
    ) -> console.RenderResult:
        """Build a Rich renderable to render the Figlet text."""
        size = min(options.max_width / 2, options.max_height)
        if size < 4:
            yield Text(self.text, style="bold")
        else:
            if size < 7:
                font_name = "mini"
            elif size < 8:
                font_name = "small"
            elif size < 10:
                font_name = "standard"
            else:
                font_name = "big"
            font = Figlet(font=font_name, width=options.max_width)
            yield Text(font.renderText(self.text).rstrip("\n"), style="bold")


class SlotButton(Button):

    clicked: Reactive[RenderableType] = Reactive(False)

    def on_click(self) -> None:
        self.clicked = True


class GameStatus(Enum):
    IDLE = 0
    GAMING = 1
    BUSTED = 2
    WIN = 3


class Game(GridView):

    DISABLED = "white on rgb(96,96,96)"
    DARK = "white on rgb(51,51,51)"
    LIGHT = "black on rgb(165,165,165)"
    YELLOW = "white on rgb(255,159,7)"

    def set_controller(self, controller: GameController):
        self.controller = controller

    @staticmethod
    def make_static(text: str, style: str) -> Static:
        """Create a static with the given Figlet label."""
        # return Static(FigletText(text), style=style, name=text)
        return SlotButton(FigletText(text), name=text, style=style)

    def on_mount(self) -> None:

        self.grid.set_gap(1, 1)
        self.grid.set_gutter(1)
        self.grid.set_align("center")

        # Create rows / columns / areas
        self.grid.add_column("col", repeat=5, size=20)
        self.grid.add_row("extract", repeat=1, size=10)
        self.grid.add_row("slots", repeat=1, size=10)
        self.grid.add_row("t_slots", repeat=1, size=10)  # DELETE
        self.grid.add_row("buttons", repeat=1, size=5)

        self.extracted = self.make_static(str("-"), self.LIGHT)
        self.total = self.make_static("0", self.LIGHT)

        first_row = [
            self.extracted,
            self.make_static("", self.DARK),
            self.make_static("", self.DARK),
            self.make_static("", self.DARK),
            self.total,
        ]

        self.slots = [
            SlotButton(FigletText("0"), name="slot_0", style=self.YELLOW),
            SlotButton(FigletText("0"), name="slot_1", style=self.YELLOW),
            SlotButton(FigletText("0"), name="slot_2", style=self.YELLOW),
            SlotButton(FigletText("0"), name="slot_3", style=self.YELLOW),
            SlotButton(FigletText("0"), name="slot_4", style=self.YELLOW),
        ]

        # TMP DELETE
        self.slots_real_value = [
            SlotButton(FigletText("0"), name="t_slot_0", style=self.YELLOW),
            SlotButton(FigletText("0"), name="t_slot_1", style=self.YELLOW),
            SlotButton(FigletText("0"), name="t_slot_2", style=self.YELLOW),
            SlotButton(FigletText("0"), name="t_slot_3", style=self.YELLOW),
            SlotButton(FigletText("0"), name="t_slot_4", style=self.YELLOW),
        ]

        self.start_btn = SlotButton("[b]START[/b]", name="start_btn", style=self.LIGHT)
        self.cash_btn = SlotButton("[b]CASH[/b]", name="cash_btn", style=self.LIGHT)

        third_row = [
            self.start_btn,
            self.make_static("", self.DARK),
            self.make_static("", self.DARK),
            self.make_static("", self.DARK),
            self.cash_btn,
        ]

        self.grid.place(*first_row)
        self.grid.place(*self.slots)
        self.grid.place(*self.slots_real_value)  # DELETE
        self.grid.place(*third_row)

        self.sounds = Sounds()

        self.status = GameStatus.IDLE

    def draw_a_card(self):
        self.extracted_value = self.controller.model.draw_a_card()
        self.extracted.label = FigletText(f"{self.extracted_value[0]}")

    def update_total(self):
        self.total.label = FigletText(f"{self.controller.get_total()}")

    def update_slot(self, slot_id, card_value) -> bool:

        slot_id = int(slot_id)
        busted = self.controller.add_card_to_slot(slot_id, card_value)
        (
            shown_value,
            real_value,
            is_flashing,
            is_busted,
        ) = self.controller.get_slot_values(slot_id)

        if is_flashing:  # TODO CHANGE BUTTON STYLE
            shown_value = f"{shown_value}*"

        self.slots[slot_id].label = FigletText(str(shown_value))
        self.slots_real_value[slot_id].label = FigletText(str(real_value))  # DELETE

        return busted or is_busted

    def write_on_slots(self, text: str):
        if len(text) <= 5:
            chars = text.__iter__()
            for i, char in enumerate(chars):
                self.slots[i].label = FigletText(char)

    # DELETEME
    def write_on_t_slots(self, text: str):
        if len(text) <= 5:
            chars = text.__iter__()
            for i, char in enumerate(chars):
                self.slots_real_value[i].label = FigletText(char)

    def handle_busted(self):
        self.status = GameStatus.BUSTED
        self.write_on_slots("BOOM!")
        self.sounds.play_loser()

    def handle_winning(self, winnings):
        self.status = GameStatus.WIN
        self.write_on_slots(f"WIN{winnings:02d}")
        self.sounds.play_winner(winnings)

    def restart(self):
        self.controller.restart()
        self.write_on_slots("00000")
        self.write_on_t_slots("00000")  # DEBUG
        self.update_total()

    def handle_button_pressed(self, message: ButtonPressed) -> None:
        """A message sent by the submit button"""
        assert isinstance(message.sender, Button)
        button_name = message.sender.name
        self.submit = message.sender.clicked

        if self.submit:
            match button_name:
                case "slot_0" | "slot_1" | "slot_2" | "slot_3" | "slot_4":
                    if self.status == GameStatus.GAMING:
                        slot_id = button_name.split("_")[1]  # this is safe

                        busted = self.update_slot(slot_id, self.extracted_value[1])

                        if busted is True:
                            self.handle_busted()
                        else:
                            self.update_total()
                            self.draw_a_card()
                            if self.controller.check_will_be_busted(
                                self.extracted_value[1]
                            ):
                                winning_value = self.controller.get_winning_value()
                                if winning_value is None:
                                    self.handle_busted()
                                else:
                                    self.handle_winning(winning_value)
                case "start_btn":
                    if self.status == GameStatus.IDLE:
                        self.status = GameStatus.GAMING
                        self.draw_a_card()
                    elif (
                        self.status == GameStatus.BUSTED
                        or self.status == GameStatus.WIN
                    ):
                        self.restart()
                        self.status = GameStatus.GAMING
                        self.draw_a_card()

                case "cash_btn":
                    winning_value = self.controller.get_winning_value()
                    if winning_value is None:
                        pass
                    else:
                        self.handle_winning(winning_value)

                    # TODO update game status method
                case _:
                    pass


class GameApp(App):
    def __init__(self, *args, controller, **kwargs):
        self.controller = controller
        super().__init__(*args, **kwargs)

    async def on_mount(self) -> None:
        self.game = Game()
        self.game.set_controller(self.controller)
        await self.view.dock(self.game)
