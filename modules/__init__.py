import gettext
import locale
import os

import tomli

from modules.paths import Paths

with open(os.path.join(Paths.base, "pyproject.toml"), "rb") as proj_file:
    _METADATA = tomli.load(proj_file)
    __package_name__ = _METADATA["project"]["name"]
    __version__ = _METADATA["project"]["version"]
    __author_name__ = _METADATA["project"]["authors"][0]["name"]
    __author_email__ = _METADATA["project"]["authors"][0]["email"]
    __githash__ = _METADATA["tool"]["myproject"]["githash"]


CURRENT_LOCALE, _ = locale.getlocale()
if CURRENT_LOCALE == "Italian_Italy":
    CURRENT_LOCALE = "it_IT"
else:
    CURRENT_LOCALE = "en_US"

locale_path = Paths.locales
dictionary = gettext.translation("messages", locale_path, [CURRENT_LOCALE])
dictionary.install()
_ = dictionary.gettext
