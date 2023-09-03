from customtkinter import CTkFrame, CTkLabel, CTkFont, CTkScrollableFrame, CTkButton, CTkToplevel, CTkEntry
from simra.utils import add_logo


class HomePage(CTkScrollableFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(fg_color='transparent', scrollbar_button_color='white', scrollbar_button_hover_color='white')
        self.columnconfigure(0, weight=1)

        self.areas: list[str] = []

        self.settings = CTkLabel(self, text="")

        add_logo(self, px=(10, 0))

        self.frame = CTkFrame(self, fg_color='deep sky blue')
        self.frame.grid(row=1, column=0, padx=(10, 0), pady=10, sticky='ew')
        self.frame.columnconfigure(0, weight=1)

        self.hello = CTkLabel(self.frame, text="Hello Emkay", font=CTkFont(weight='bold', size=24, family='monospaced'))
        self.hello.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='ew')
        self.hello.configure(text_color='white')

        self.email_lb = CTkLabel(self.frame, text="emkay.py@gmail.com")
        self.email_lb.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='ew')
        self.email_lb.configure(text_color='white')

        self.add_new_loc_btn = CTkButton(self, text="+ Add new location", fg_color='lime green')
        self.add_new_loc_btn.grid(row=3, column=0, padx=(10, 0), pady=(0, 10), sticky='ew')
        self.add_new_loc_btn.configure(hover_color='lime', height=40, font=CTkFont(weight='bold'), cursor='hand2')
        self.add_new_loc_btn.configure(command=self.add_area)

        self.add_area("Soshanguve-L")

    def add_area(self, name: str = None) -> None:
        # AreaAdd()
        area_btn = CTkButton(self, text=name, fg_color='grey90', hover_color='grey80', height=40)
        area_btn.configure(text_color='grey25', font=CTkFont(weight='bold'), cursor='hand2')
        area_btn.configure(command=lambda: self.open_area(name if name is not None else ''))
        self.add_new_loc_btn.grid_forget()
        area_btn.grid(row=len(self.areas) + 3, column=0, padx=(10, 0), pady=(0, 10), sticky='ew')
        self.add_new_loc_btn.grid(row=len(self.areas) + 4, padx=(10, 0), pady=(0, 10), sticky='ew')
        self.areas.append(name)

    def open_area(self, name: str) -> None:
        self.grid_forget()
        # area = AreaFrame(self, name=name)
        # area.grid(row=0, column=0, sticky='nsew')
        #
        # add_logo(area)
        #
        # title = CTkLabel(area, text=name)
        # title.grid(row=0, column=0, padx=(10, 0), pady=(0, 10), sticky='w')


class AreaAdd(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = CTkEntry(self, corner_radius=20, placeholder_text="Area name")
        self.name.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        self.master.wait_window(self)
