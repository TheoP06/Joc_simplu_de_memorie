import os
import random

class ImageGenerator:
    def __init__(self, image_folder):
        self.image_folder = image_folder

    def load_images(self):
        valid_extensions = (".png",)
        files = sorted([f for f in os.listdir(self.image_folder) if f.lower().endswith(valid_extensions)])

        images = []
        pair_counter = 1

        for i in range(0, len(files), 2):
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
