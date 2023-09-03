from customtkinter import CTkScrollableFrame, CTkLabel, CTkFont, CTkButton
# from ..utils import add_logo


class AreaFrame(CTkScrollableFrame):
    def __init__(self, *args, name: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(scrollbar_button_hover_color='white', scrollbar_button_color='white')
        self.name: str = name
        self.num_cases: int = 0

        # add_logo(self)

        self.title = CTkLabel(self, text=name.title())
        self.title.configure(font=CTkFont(weight='bold', family='monospaced'))
        self.title.grid(row=0, column=0, padx=10, pady=(0, 10))

        self.report_btn = CTkButton(self, text="Report HS2 test")
        self.report_btn.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='w')
