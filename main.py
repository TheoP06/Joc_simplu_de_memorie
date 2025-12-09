import tkinter as tk
from PIL import Image, ImageTk
from image_generator import ImageGenerator

def main():
    img_gen = ImageGenerator("images")
    pairs = img_gen.generate_pairs()

    root = tk.Tk()
    root.title("Joc simplu de memorie")

    rows = 4
    cols = 3

    photo_images = []

    for idx, card in enumerate(pairs):
        img = Image.open(card["file_path"])
        img = img.resize((160, 90))
        photo = ImageTk.PhotoImage(img)
        photo_images.append(photo)

        label = tk.Label(root, image=photo, compound="top")
        label.grid(row=idx // cols, column=idx % cols, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
