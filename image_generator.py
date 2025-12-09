import os
import random
from PIL import Image

class ImageGenerator:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def generate_pairs(self):
        """
        Încarcă toate imaginile PNG din folder și creează perechi.
        Fiecare pereche are două carduri cu pair_id identic.
        """
        # Obține toate fișierele PNG din folder
        files = [f for f in os.listdir(self.folder_path) if f.lower().endswith(".png")]
        files.sort()

        if not files:
            print(f"[EROARE] Nu s-au găsit fișiere PNG în {self.folder_path}")
            return []

        cards = []
        pair_id = 1

        for i in range(0, len(files), 2):
            if i + 1 >= len(files):
                break  # protecție dacă e număr impar de imagini
            path1 = os.path.join(self.folder_path, files[i])
            path2 = os.path.join(self.folder_path, files[i+1])

            card1 = {"id": f"{files[i]}_1", "image_path": path1, "pair_id": pair_id}
            card2 = {"id": f"{files[i+1]}_2", "image_path": path2, "pair_id": pair_id}

            cards.extend([card1, card2])
            pair_id += 1

        random.shuffle(cards)
        return cards
