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
from modules.game_view_mod import GameView


current_locale, _ = locale.getlocale()
if current_locale == "Italian_Italy":
    current_locale = "it_IT"
locale_path = os.path.join("files", "locale")
dictionary = gettext.translation("main", locale_path, [current_locale])
dictionary.install()
_ = dictionary.gettext


def main():
    model = GameModel()
    view = GameView()

    controller = GameController(model, view)

    view.set_controller(controller)

    controller.start_game()


if __name__ == "__main__":

    FORMAT = "%(asctime)-15s `%(name)s` => '%(message)s'"
    log_file = os.path.join("files", f"{modules.__project_name__}.log")
    logging.basicConfig(filename=log_file, level=logging.INFO, format=FORMAT)
    logger = logging.getLogger("main")

    logger.info("App Started")

    main()

    logger.info("App Closed")

    sys.exit(0)
