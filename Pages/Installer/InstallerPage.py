import tkinter
from tkinter import MULTIPLE, font
from tkinter.font import BOLD
from tkinter import BOTH, LEFT, RIGHT, PhotoImage, Scrollbar, ttk

from soupsieve import select
from Helpers import JsonReader
from Helpers.ProgramsVariables import ProgramsVariables
from Pages.Installer.InstallerHelper import Helper
from Helpers import WindowCreator
from Pages.Common import BasePage

#Class that creates installer page
class Installer(BasePage.BasePage):
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x500")
        self.master.resizable(0,0)
        self.json_file = JsonReader.JsonHelper()
        self.programs_variables = ProgramsVariables(len(self.json_file.json_keys))
        self.base_page = BasePage.BasePage(self.master)
        self.create_frames()
        self.installer_helper = Helper(self.json_file, self.programs_variables, self)
        self.create_labels()
        self.create_buttons()
        self.create_progressBar()

    #Create all frames in the page
    def create_frames(self):
        self.middle_frame = tkinter.Frame(height = 400, width = 300, bg = "white")
        self.middle_frame.propagate(0) 
        self.middle_frame.pack(fill='both', side='right', expand='True',)

        self.upper_frame = tkinter.Frame(self.middle_frame, height = 100, width = 100) 
        self.upper_frame.propagate(0) 
        self.upper_frame.pack(fill='both', side='top', expand='False')

        self.bottom_frame = tkinter.Frame(self.middle_frame,height = 100, width = 100)
        self.bottom_frame.propagate(0) 
        self.bottom_frame.pack(fill='x', side='bottom', expand='False')

        self.canvas = tkinter.Canvas(self.middle_frame, background="white")
        self.v = Scrollbar(self.canvas, command=self.canvas.yview)

    #Create all labels in the page
    def create_labels(self):
        tkinter.Label(self.upper_frame, text="Instalar Aplicativos", font=("Arial", 20, BOLD)).place(relx=0.0, rely=0.3)

        tkinter.Label(self.upper_frame, text="Selecionar Todos", font=("Arial", 8, BOLD)).place(relx=0.0, rely=0.8)
        self.select_all = tkinter.Checkbutton(self.upper_frame, command=self.installer_helper.install_all_programs).place(relx=0.21, rely=0.79)
        tkinter.Label(self.upper_frame, text="Selecionar Básicos", font=("Arial", 8, BOLD)).place(relx=0.25, rely=0.8)
        self.select_basic = tkinter.Checkbutton(self.upper_frame, command=self.installer_helper.install_basic_programs).place(relx=0.48, rely=0.79)
        tkinter.Label(self.upper_frame, text="Selecionar Essenciais", font=("Arial", 8, BOLD)).place(relx=0.52, rely=0.8)
        self.select_essential = tkinter.Checkbutton(self.upper_frame, command=self.installer_helper.install_essential_programs).place(relx=0.79, rely=0.79)

        self.download_label = tkinter.Label(self.bottom_frame, text="", font=("Arial", 10))
        self.download_label.place(relx=0)

        position = 0

        for program_element in self.json_file.json_keys:
            selected = self.programs_variables.programs_selected[position] == 1
            self.programs_variables.programs_selected[position] = tkinter.IntVar()

            self.img_icon_installer = PhotoImage(file=self.json_file.data[program_element]["icone"])
            self.label = tkinter.Label(self.canvas, text=self.json_file.data[program_element]["nome"], font=("Arial",10, BOLD), image=self.img_icon_installer,compound=LEFT,background="white")
            self.label.image = self.img_icon_installer  
            
            self.canvas.create_window(0, (position+1)*30, anchor='nw', window=self.label, height=25)
            self.canvas.create_line(0, 25 + (position+1)*30, 500, 25 + (position+1)*30)
            self.checkButton = tkinter.Checkbutton(self.canvas, background="white", variable=self.programs_variables.programs_selected[position], bd=0)
            self.canvas.create_window(350, (position+1)*30, anchor='nw', window=self.checkButton, height=25)
            if(selected):
                self.programs_variables.programs_selected[position].set(1)

            position += 1
        
        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.v.set)
        self.canvas.pack(fill=BOTH, expand=True,)
        self.v.pack(side= 'right', fill='y')

    #Create all buttons in the page
    def create_buttons(self): 
        img_download = PhotoImage(file="Assets/Images/download-direto.png")
        self.download_button = tkinter.Button(self.bottom_frame, image=img_download, borderwidth=0, cursor="hand2", command=self.installer_helper.download)
        self.download_button.image = img_download
        self.download_button.place(relx=0.85, rely=0.2)

        img_plus = PhotoImage(file="Assets/Images/plus.png")
        self.add_button = tkinter.Button(self.upper_frame,image=img_plus, borderwidth=0, cursor="hand2", command= lambda: WindowCreator.WindowCreator.access_add_program_page(self.master))
        self.add_button.image = img_plus
        self.add_button.place(relx=0.9, rely=0.6)

    #Create the progressbar
    def create_progressBar(self):
        self.pb = ttk.Progressbar(self.bottom_frame, orient='horizontal', mode='determinate', length=350)
        self.pb["value"] = 0
        self.pb["maximum"] = 100
        self.pb.grid(column=0, row=0, columnspan=2, pady=30)