import threading
from playsound import playsound
import os


class Sounds:

    _files_path = "./files/sounds/"
    _sounds = {
        "loser": "loser.mp3",
        "coin_drop": "coin_drop.mp3",
        "draw_Card": "draw_card.mp3",
    }

    def play_loser(self):
        self.play("loser")

    def play_winner(self, loop_no):
        self.play("coin_drop", loop_no)

    def play_draw_card(self):
        self.play("draw_Card")

    def play_sound(self, path, loop_no):
        for _ in range(0, loop_no):
            playsound(path)

    def play(self, sound, loop_no=1):
        sound_path = self._sounds[sound]
        if sound_path:
            threading.Thread(
                target=self.play_sound,
                args=(os.path.join(self._files_path, sound_path), loop_no),
                daemon=True,
            ).start()
