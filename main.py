import os
import tkinter as tk
from PIL import Image, ImageTk
from image_generator import ImageGenerator

def main():
    folder_path = r"C:\Users\teodo\Documents\Protiect Python 19"  # folder cu imaginile tale PNG
    img_gen = ImageGenerator(folder_path)
    pairs = img_gen.generate_pairs()

    if not pairs:
        print("Nu există imagini de afișat.")
        return

    root = tk.Tk()
    root.title("Joc simplu de memorie")

    cols = 3
    photo_images = []

    for idx, card in enumerate(pairs):
        img = Image.open(card["image_path"])
        img = img.resize((160, 90))  # redimensionare opțională
        photo = ImageTk.PhotoImage(img)
        photo_images.append(photo)

        label = tk.Label(root, image=photo)
        label.grid(row=idx // cols, column=idx % cols, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
