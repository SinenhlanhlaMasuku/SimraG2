from customtkinter import CTkLabel, CTkImage
from PIL import Image
from os import path
path: str = path.dirname(path.abspath(__file__))


def add_logo(master, row=0, col=0, px=10, py=10) -> None:
    image = CTkLabel(master, text="", image=CTkImage(
        dark_image=Image.open(fr'{path}\images\logo.png'), size=(100, 100)))
    image.grid(row=row, column=col, padx=px, pady=py, sticky='ew')
    return None
