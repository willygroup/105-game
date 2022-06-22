import threading
from playsound import playsound
import os


class Sounds:

    _files_path = "./files/sounds/"
    _sounds = {"loser": "loser.mp3"}

    def play_loser(self):
        self.play("loser")

    def play(self, sound):
        sound_path = self._sounds[sound]
        if sound_path:
            threading.Thread(
                target=playsound,
                args=(os.path.join(self._files_path, sound_path),),
                daemon=True,
            ).start()
