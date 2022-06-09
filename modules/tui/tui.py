from rich import console
from textual.app import App
from textual.views import GridView
from rich.text import Text
from textual.widgets import Button, Static, Placeholder
from pyfiglet import Figlet


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


class Game(GridView):

    DARK = "white on rgb(51,51,51)"
    LIGHT = "black on rgb(165,165,165)"
    YELLOW = "white on rgb(255,159,7)"

    def on_mount(self) -> None:
        self.grid.set_gap(1, 1)
        self.grid.set_gutter(1)
        self.grid.set_align("center")

        # # Create rows / columns / areas
        self.grid.add_column("col", repeat=5, size=20)
        self.grid.add_row("extract", repeat=1, size=10)
        self.grid.add_row("slots", repeat=1, size=10)
        self.grid.add_row("buttons", repeat=1, size=5)

        # self.grid.add_areas(
        #     extract="col1-start|col2-end,row1,extract",
        #     total="col4-start|col5-end,row1,total",
        #     slots="col1-start|col5-end,row2,slots",
        #     buttons="col1-start|col5-end,row3",
        # )

        def make_static(text: str, style: str) -> Button:
            """Create a static with the given Figlet label."""
            return Static(FigletText(text), style=style, name=text)

        def make_button(text: str, style: str) -> Button:
            """Create a button with the given Figlet label."""
            return Button(FigletText(text), style=style, name=text)

        first_row = [
            make_static("A", self.LIGHT),
            make_static("", self.DARK),
            make_static("", self.DARK),
            make_static("", self.DARK),
            make_static("105", self.LIGHT),
        ]

        second_row = [make_button("0", self.YELLOW) for _ in range(0, 5)]
        third_row = [
            Button("[b]START[/b]", self.LIGHT),
            make_static("", self.DARK),
            make_static("", self.DARK),
            make_static("", self.DARK),
            Button("[b]CASH[/b]", self.LIGHT),
        ]

        self.grid.place(*first_row)
        self.grid.place(*second_row)
        self.grid.place(*third_row)


class GameApp(App):
    async def on_mount(self) -> None:
        await self.view.dock(Game())


GameApp.run(
    title="Calculator Test",
)
