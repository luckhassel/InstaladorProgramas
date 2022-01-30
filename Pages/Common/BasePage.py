import tkinter
from tkinter.font import BOLD
from tkinter import BOTH, LEFT, RIGHT, PhotoImage, Scrollbar, ttk
from Helpers import WindowCreator
from Helpers import UserData

class BasePage:

    def __init__(self, master):
        self.master = master
        self.user_data = UserData.UserData.get_instance()
        self.create_frames()
        self.create_labels()
        self.create_buttons()

    def create_frames(self):
        self.left_frame = tkinter.Frame(height = 200, width = 50, bg = "white", padx=10, pady=30)
        self.left_frame.propagate(0) 
        self.left_frame.pack(fill='both', side='left', expand='True', padx=10, pady=30)

    def create_labels(self):
        tkinter.Label(self.left_frame, text=self.user_data.user_name, font=("Arial", 10, BOLD), background="white").place(relx=0.25, rely=0.3)
        tkinter.Label(self.left_frame, text="Técnico", font=("Arial", 8, BOLD), background="white").place(relx=0.35, rely=0.35)

        img_user = PhotoImage(file="Assets/Images/man.png")
        self.img_profile = tkinter.Label(self.left_frame, image=img_user, background="white", borderwidth=0)
        self.img_profile.image = img_user
        self.img_profile.place(relx=0.25, rely=0.0)

    def create_buttons(self):
        img_settings = PhotoImage(file="Assets/Images/settings.png")
        add_button = tkinter.Button(self.left_frame, text=" CONFIGURAR WINDOWS" ,image=img_settings, compound=LEFT, background="white", borderwidth=0, cursor="hand2")
        add_button.image = img_settings
        add_button.place(rely=0.5)
        
        img_install = PhotoImage(file="Assets/Images/seta-para-download.png")
        self.install_button = tkinter.Button(self.left_frame, text=" INSTALAR APLICATIVOS",image=img_install, compound=LEFT, bg='white', borderwidth=0, cursor="hand2", command=lambda: WindowCreator.WindowCreator.access_installer_page(self.master))
        self.install_button.image = img_install
        self.install_button.place(relx=0.05, rely=0.6) 

        img_user = PhotoImage(file="Assets/Images/user.png")
        self.profile_button = tkinter.Button(self.left_frame, text="   CONFIGURAR PERFIL", image=img_user, compound=LEFT, background="white", borderwidth=0, cursor="hand2")
        self.profile_button.image = img_user
        self.profile_button.place(relx=0.05, rely=0.7) 
        
        img_exit = PhotoImage(file="Assets/Images/exit.png")
        self.exit_button = tkinter.Button(self.left_frame, image=img_exit, background="white", borderwidth=0, cursor="hand2", command=lambda: WindowCreator.WindowCreator.exit_app(self.master))
        self.exit_button.image = img_exit
        self.exit_button.place(relx=0.9, rely=1.0) 