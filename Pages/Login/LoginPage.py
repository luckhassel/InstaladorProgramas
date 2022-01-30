import tkinter
from tkinter.font import BOLD
from tkinter import BOTH, LEFT, RIGHT, PhotoImage, Scrollbar, ttk
from Helpers import WindowCreator
import hashlib
import pyodbc
from Helpers import ConnectionString
from Helpers import UserData

#Creates login page
class Login:

    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.resizable(0,0)
        self.user_data = UserData.UserData()
        self.create_frames()
        self.create_labels()
        self.create_buttons()
        self.create_text_box()

    def create_frames(self):
        self.left_frame = tkinter.Frame(height = 200, width = 50, bg = "white", padx=10, pady=30)
        self.left_frame.propagate(0) 
        self.left_frame.pack(fill='both', side='left', expand='True')
        self.master.bind('<Return>', self.__login)

    def create_labels(self):
        tkinter.Label(self.left_frame, text="Usuário", font=("Arial", 10, BOLD), background="white").place(relx=0.25, rely=0.55)
        tkinter.Label(self.left_frame, text="Senha", font=("Arial", 10, BOLD), background="white").place(relx=0.25, rely=0.75)
        self.error_message = tkinter.Label(self.left_frame, font=("Arial", 8), background="white")
        self.error_message.place(relx=0.25, rely=0.85)

        img_user = PhotoImage(file="Assets/Images/logo.png")
        self.img_profile = tkinter.Label(self.left_frame, image=img_user, background="white", borderwidth=0)
        self.img_profile.image = img_user
        self.img_profile.place(relx=0.35, rely=0.05)

    def create_buttons(self):
        img_exit = PhotoImage(file="Assets/Images/exit.png")
        self.exit_button = tkinter.Button(self.left_frame, image=img_exit, background="white", borderwidth=0, cursor="hand2", command=lambda: WindowCreator.WindowCreator.exit_app(self.master))
        self.exit_button.image = img_exit
        self.exit_button.place(relx=0.95, rely=1)

        img_login = PhotoImage(file="Assets/Images/login.png")
        self.img_login = tkinter.Button(self.left_frame, image=img_login, background="white", borderwidth=0, cursor="hand2", command=lambda: self.__login())
        self.img_login.image = img_login
        self.img_login.place(relx=0.48, rely=0.9) 
    
    def create_text_box(self):
        self.username = tkinter.Entry(self.left_frame, width = 30, background="#EEEEEE", borderwidth=0, font=("Trebuchet MS", 12))
        self.username.place(rely=0.6, relx=0.25)
        self.password = tkinter.Entry(self.left_frame, width = 30, background="#EEEEEE", show="*", borderwidth=0,  font=("Trebuchet MS", 12))
        self.password.place(rely=0.8, relx=0.25)

    #Check with database if data matches
    def __login(self, event=None):
        name_value = self.username.get()
        password_value = self.password.get()
        hashed_password = hashlib.md5(password_value.encode('utf8')).hexdigest()

        print(name_value)
        print(hashed_password)

        with pyodbc.connect('DRIVER='+ConnectionString.driver+';SERVER=tcp:'+ConnectionString.server+';PORT=1433;DATABASE='+ConnectionString.database+';UID='+ConnectionString.username+';PWD='+ ConnectionString.password) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {ConnectionString.table}")
                row = cursor.fetchone()
                while row:
                    sql_name = str(row[1])
                    sql_password = str(row[2])
                    print (str(row[1]) + " " + str(row[2]))
                    row = cursor.fetchone()

        if (name_value == sql_name and hashed_password == sql_password):
            self.user_data.set_user_name(sql_name)
            WindowCreator.WindowCreator.access_installer_page(self.master)
        else:
            self.error_message['text'] = "Usuário e/ou Senha incorreto(s)"