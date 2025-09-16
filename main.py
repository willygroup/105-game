#! /usr/bin/env python
"""
105-Game
"""

import gettext
import locale
import logging
import os
import sys
import modules
from modules.game_controller_mod import GameController

from modules.game_model_mod import GameModel
from modules.gui.tui import GameApp
from modules.paths import Paths


def main(debug_mode: bool):
    model = GameModel()

    controller = GameController(model)

    view = GameApp(
        controller=controller, debug_mode=debug_mode, log=Paths.file("105-game.log")
    )

    controller.set_view(view)

    view.run()


if __name__ == "__main__":

    debug_mode = False
    if "--debug" in sys.argv:
        print("DEBUG MODE")
        debug_mode = True

    FORMAT = "%(asctime)-15s `%(name)s` => '%(message)s'"
    log_file = os.path.join("files", f"{modules.__package_name__}.log")
    logging.basicConfig(filename=log_file, level=logging.INFO, format=FORMAT)
    logger = logging.getLogger("main")

    logger.info("App Started")

    main(debug_mode)

    logger.info("App Closed")

    sys.exit(0)
