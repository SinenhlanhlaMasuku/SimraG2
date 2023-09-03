from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkCheckBox, CTkButton
from customtkinter import CTkFont
from simra.utils import add_logo
import re
from tkinter import messagebox as msg


class RegisterFrame(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)

        add_logo(self)

        self.email = self.add_entry('Email', 1)
        self.password = self.add_entry('Password', 2, False)
        self.confirm_pass = self.add_entry("Confirm Password", 3, False)
        self.first_name = self.add_entry('First name', 4)
        self.last_name = self.add_entry('Last name', 5)
        self.municipality = self.add_entry('Municipality', 6)

        self.frame = CTkFrame(self, fg_color='transparent')
        self.frame.grid(row=7, column=0, sticky='ew')

        self.agree = CTkCheckBox(self.frame, text="Agree to terms and conditions")
        self.agree.grid(row=0, column=0, padx=10, pady=(0, 10), sticky='w')
        self.agree.configure(corner_radius=4, hover=False)

        self.next = CTkButton(self.frame, text=">", fg_color='transparent', hover=False)
        self.next.configure(text_color='deep sky blue', font=CTkFont(weight='bold', size=20))
        self.next.grid(row=0, column=1, sticky='new')
        self.next.configure(command=self.next_page, height=36)

    def add_entry(self, ph: str, row: int, visible=True) -> CTkEntry:
        entry = CTkEntry(self, corner_radius=16, border_width=0, placeholder_text=ph)
        entry.configure(fg_color="grey90", height=36, show='' if visible else '●')
        entry.grid(row=row, column=0, padx=10, pady=(0, 20), sticky='ew')
        return entry

    def next_page(self) -> None:
        # if not self.email_valid():
        #     msg.showwarning(message="Invalid email")
        # elif not self.password_valid():
        #     msg.showwarning(message="Password should be at least 6 characters and match confirm password")
        # elif not self.inputs_valid():
        #     msg.showwarning(message="Invalid inputs")
        # else:
        self.master.show('home_page')
        return None

    def inputs_valid(self) -> bool:
        return self.first_name.get() != '' and self.last_name.get() != '' and self.municipality.get() != ''

    def email_valid(self) -> bool:
        pattern = r'^\S+@\S+\.\S+$'
        return bool(re.match(pattern, self.email.get()))

    def password_valid(self) -> bool:
        return len(self.password.get()) >= 6 and (self.password.get() == self.confirm_pass.get())

