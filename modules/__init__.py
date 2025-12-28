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


current_locale, _ = locale.getlocale()
if current_locale == "Italian_Italy":
    current_locale = "it_IT"
else:
    current_locale = "en_US"

dictionary = gettext.translation("main", Paths.locales, [current_locale])

dictionary.install()
_ = dictionary.gettext
