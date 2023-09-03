from customtkinter import CTkFrame, CTkImage, CTkLabel, CTkFont, CTkButton
from os import path
from PIL import Image

path: str = path.dirname(path.abspath(__file__))


class InitialFrame(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)

        self.image = CTkLabel(self, text="", image=CTkImage(
            dark_image=Image.open(fr'{path}\..\images\logo.png'), size=(120, 120)))
        self.image.grid(row=0, column=0, padx=10, pady=30, sticky='ew')

        self.label = CTkLabel(self, text="Welcomes you to a healthier water consumption.")
        self.label.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.label.configure(font=CTkFont(size=18), wraplength=320)

        self.button = CTkButton(self, text="SIGN UP", width=140, height=36)
        self.button.grid(row=2, column=0, padx=30, pady=(70, 10))
        self.button.configure(corner_radius=4, font=CTkFont(weight='bold'), cursor='hand2')
        self.button.configure(command=self.show_signup)

    def show_signup(self):
        self.master.show('signup')
        return None
