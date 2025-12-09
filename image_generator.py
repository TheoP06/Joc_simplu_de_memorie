import os
import random

class ImageGenerator:
    def __init__(self, image_folder):
        self.image_folder = image_folder

    def load_images(self):
        if not os.path.exists(self.image_folder):
            print(f"[EROARE] Folderul '{self.image_folder}' nu există.")
            return []

        valid_extensions = (".png",)
        files = sorted([f for f in os.listdir(self.image_folder) if f.lower().endswith(valid_extensions)])

        if not files:
            print(f"[EROARE] Nu s-au găsit imagini PNG în folderul '{self.image_folder}'.")
            return []

        images = []
        pair_counter = 1

        for i in range(0, len(files), 2):
            if i + 1 >= len(files):  # protecție dacă e număr impar
                break
            img1 = {
                "id": i + 1,
                "file_path": os.path.join(self.image_folder, files[i]),
                "description": os.path.splitext(files[i])[0],
                "pair_id": pair_counter
            }
            img2 = {
                "id": i + 2,
                "file_path": os.path.join(self.image_folder, files[i + 1]),
                "description": os.path.splitext(files[i + 1])[0],
                "pair_id": pair_counter
            }
            images.extend([img1, img2])
            pair_counter += 1

        return images

    def generate_pairs(self):
        images = self.load_images()
        random.shuffle(images)
        return images
