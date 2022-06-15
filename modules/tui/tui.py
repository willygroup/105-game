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
    IDLE = (0,)
    GAMING = (1,)
    BUSTED = 2


class Game(GridView):

    DISABLED = "white on rgb(96,96,96)"
    DARK = "white on rgb(51,51,51)"
    LIGHT = "black on rgb(165,165,165)"
    YELLOW = "white on rgb(255,159,7)"

    def set_controller(self, controller: GameController):
        self.controller = controller

    def on_mount(self) -> None:

        # self.extracted_value = 3

        self.grid.set_gap(1, 1)
        self.grid.set_gutter(1)
        self.grid.set_align("center")

        # Create rows / columns / areas
        self.grid.add_column("col", repeat=5, size=20)
        self.grid.add_row("extract", repeat=1, size=10)
        self.grid.add_row("slots", repeat=1, size=10)
        self.grid.add_row("buttons", repeat=1, size=5)

        def make_static(text: str, style: str) -> Static:
            """Create a static with the given Figlet label."""
            return Static(FigletText(text), style=style, name=text)

        self.extracted = make_static(str("-"), self.LIGHT)
        self.total = make_static("105", self.LIGHT)

        first_row = [
            self.extracted,
            make_static("", self.DARK),
            make_static("", self.DARK),
            make_static("", self.DARK),
            self.total,
        ]

        slot_0 = SlotButton(FigletText("0"), name="slot_0", style=self.YELLOW)
        slot_1 = SlotButton(FigletText("0"), name="slot_1", style=self.YELLOW)
        slot_2 = SlotButton(FigletText("0"), name="slot_2", style=self.YELLOW)
        slot_3 = SlotButton(FigletText("0"), name="slot_3", style=self.YELLOW)
        slot_4 = SlotButton(FigletText("0"), name="slot_4", style=self.YELLOW)
        self.slots = [
            slot_0,
            slot_1,
            slot_2,
            slot_3,
            slot_4,
        ]

        self.start_btn = SlotButton("[b]START[/b]", name="start_btn", style=self.LIGHT)
        self.cash_btn = SlotButton("[b]CASH[/b]", self.LIGHT)

        third_row = [
            self.start_btn,
            make_static("", self.DARK),
            make_static("", self.DARK),
            make_static("", self.DARK),
            self.cash_btn,
        ]

        self.grid.place(*first_row)
        self.grid.place(*self.slots)
        self.grid.place(*third_row)

        self.status = GameStatus.IDLE

    def draw_a_card(self):
        self.extracted_value = self.controller.model.draw_a_card()
        self.extracted.label = FigletText(f"{self.extracted_value}")

    def update_slot(self, slot_id, card_value) -> bool:
        slot_id = int(slot_id)
        busted = self.controller.add_card_to_slot(slot_id, card_value)
        (shown_value, is_flashing, is_busted) = self.controller.get_slot_values(slot_id)

        if is_flashing:  # TODO CHANGE BUTTON STYLE
            shown_value = f"{shown_value}*"

        self.slots[slot_id].label = FigletText(str(shown_value))

        return busted or is_busted

    def handle_button_pressed(self, message: ButtonPressed) -> None:
        """A message sent by the submit button"""
        assert isinstance(message.sender, Button)
        button_name = message.sender.name
        self.submit = message.sender.clicked

        if self.submit:
            match button_name:
                case "slot_0" | "slot_1" | "slot_2" | "slot_3" | "slot_4":
                    slot_id = button_name.split("_")[1]  # this is safe
                    busted = self.update_slot(slot_id, self.extracted_value)
                    if busted:
                        self.status = GameStatus.BUSTED
                    else:
                        self.draw_a_card()
                case "start_btn":
                    if self.status == GameStatus.IDLE:
                        GameStatus.GAMING
                        self.draw_a_card()

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
