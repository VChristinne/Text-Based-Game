import customtkinter as ctk


class Window:
    def __init__(self, master):
        master.title("CustomTkinter")
        master.resizable(False, False)
        master.attributes('-fullscreen', True)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("./theme/nord.json")


class SideFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = ctk.CTkLabel(self, text="Testing")
        self.label.grid(row=0, column=0, padx=20, pady=20)
        

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.window = Window(self)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=2) 

        for i in range(2):
            side_frame = SideFrame(self)
            side_frame.grid(row=0, column=i, sticky="nswe")


app = App()
app.mainloop()