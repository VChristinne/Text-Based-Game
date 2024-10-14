import customtkinter as ctk


class Window:
    def __init__(self, master):
        master.title("CustomTkinter")
        master.resizable(False, False)
        master.attributes('-fullscreen', True)
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("./theme/nord.json")


class Background(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text=None)
        self.label.grid(row=0, column=0, padx=20, pady=20)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.window = Window(self)
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=4)
        self.grid_columnconfigure(index=1, weight=2) 

        for i in range(2):
            bg_frame = Background(self)
            bg_frame.grid(row=0, column=i, sticky="nswe")


app = App()
app.mainloop()