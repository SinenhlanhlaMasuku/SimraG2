from customtkinter import CTk, set_appearance_mode
from ui import InitialFrame, RegisterFrame, HomePage, AreaFrame


class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('340x500+100+100')
        self.title("Simra") # NOQA
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.configure(fg_color='white')

        self.current_frame = None

        self.init_frame = InitialFrame(self, fg_color='transparent')
        self.init_frame.grid(row=0, column=0, sticky='nsew')
        self.current_frame = self.init_frame

        self.reg_frame = RegisterFrame(self)
        self.home_page = HomePage(self)

    def show(self, frame: str):
        self.current_frame.grid_forget()
        match frame.lower():
            case 'signup':
                self.current_frame = self.reg_frame
            case 'home_page':
                self.current_frame = self.home_page

        self.current_frame.configure(fg_color='transparent')
        self.current_frame.grid(row=0, column=0, padx=0, pady=0, sticky='nsew')


if __name__ == '__main__':
    set_appearance_mode('light')
    app: App = App()
    app.mainloop()
