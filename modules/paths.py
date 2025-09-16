import os
import sys


class Paths:

    dirname = None
    if getattr(sys, "frozen", False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        dirname = sys._MEIPASS  # type: ignore

    else:
        dirname = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

    base = os.path.join(os.path.dirname(__file__), "..")
    files = os.path.join(base, "files")
    images = os.path.join(base, "files", "images")
    icons = os.path.join(base, "files", "icons")
    locales = os.path.join(base, "files", "locale")

    # File loaders.

    @classmethod
    def init(cls, directory: str) -> None:
        cls.base = directory
        cls.files = os.path.join(cls.base, "files")
        cls.images = os.path.join(cls.base, "files", "images")
        cls.icons = os.path.join(cls.base, "files", "icons")
        cls.locales = os.path.join(cls.base, "files", "locale")

    @classmethod
    def image(cls, filename: str) -> str:
        return os.path.join(cls.images, filename)

    @classmethod
    def icon(cls, filename: str) -> str:
        return os.path.join(cls.icons, filename)

    @classmethod
    def locale(cls, filename: str) -> str:
        return os.path.join(cls.locales, filename)

    @classmethod
    def file(cls, filename: str) -> str:
        return os.path.join(cls.files, filename)
