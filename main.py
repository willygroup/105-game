#! /usr/bin/env python
"""
MyProject Description
"""

import gettext
import locale
import logging
import os
import sys


__project_name__ = "myproject"

if getattr(sys, "frozen", False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    dirname = sys._MEIPASS
else:
    dirname = os.path.dirname(os.path.abspath(__file__))


current_locale, _ = locale.getlocale()
if current_locale == "Italian_Italy":
    current_locale = "it_IT"
locale_path = os.path.join("files", "locale")
dictionary = gettext.translation("main", locale_path, [current_locale])
dictionary.install()
_ = dictionary.gettext


def main():
    print("Done!")
    pass


if __name__ == "__main__":

    FORMAT = "%(asctime)-15s `%(name)s` => '%(message)s'"
    log_file = os.path.join("files", f"{__project_name__}.log")
    logging.basicConfig(filename=log_file, level=logging.INFO, format=FORMAT)
    logger = logging.getLogger("main")

    logger.info("App Started")

    main()

    logger.info("App Closed")

    sys.exit(0)
