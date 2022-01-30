from asyncio.windows_events import NULL
from cgitb import handler
import tkinter
from tkinter.font import BOLD
from tkinter import BOTH, END, LEFT, RIGHT, PhotoImage, Scrollbar, ttk
import json
from Pages.Common import BasePage
from Helpers import ImageReader
from tkinter import filedialog
from PIL import Image, ImageTk
from Helpers import JsonReader
import win32ui
import win32gui
import win32con
import win32api

#Class that created add program page
class AddProgram(BasePage.BasePage):
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x500")
        self.master.resizable(0,0)
        self.base_page = BasePage.BasePage(self.master)
        self.json_file = JsonReader.JsonHelper()
        self.create_frames()
        self.create_text_box()
        self.create_labels()
        self.create_buttons()

    #Create all frames
    def create_frames(self):
        self.middle_frame = tkinter.Frame(height = 400, width = 300, bg = "white")
        self.middle_frame.propagate(0) 
        self.middle_frame.pack(fill='both', side='right', expand='True')

        self.upper_frame = tkinter.Frame(self.middle_frame, height = 100, width = 100) 
        self.upper_frame.propagate(0) 
        self.upper_frame.pack(fill='both', side='top', expand='False')

        self.bottom_frame = tkinter.Frame(self.middle_frame,height = 100, width = 100)
        self.bottom_frame.propagate(0) 
        self.bottom_frame.pack(fill='x', side='bottom', expand='False')

    #Create all text boxes
    def create_text_box(self):
        self.program_name = tkinter.Text(self.middle_frame, height = 2, width = 50, background="#EEEEEE")
        self.program_name.place(rely=0.3, relx=0.05)
        self.program_command = tkinter.Text(self.middle_frame, height = 2, width = 50, background="#EEEEEE")
        self.program_command.place(rely=0.5, relx=0.05)

    #Create all labels
    def create_labels(self):
        tkinter.Label(self.upper_frame, text="Adicionar Programa", font=("Arial", 20, BOLD)).place(relx=0.0, rely=0.5)
        tkinter.Label(self.middle_frame, text="Nome do programa", font=("Arial", 10, BOLD), background="white").place(rely=0.25, relx=0.05)
        tkinter.Label(self.middle_frame, text="Comando para executar", font=("Arial", 10, BOLD), background="white").place(rely=0.45, relx=0.05)
        self.add_label = tkinter.Label(self.bottom_frame, font=("Arial", 10))
        self.add_label.place(rely=0.0)
    
    #Create all buttons
    def create_buttons(self):
        img_add_program = PhotoImage(file="Assets/Images/plus.png")
        self.add_program = tkinter.Button(self.bottom_frame, text="Adicionar", font=("Arial", 10, BOLD), image=img_add_program, compound=LEFT, borderwidth=0, cursor="hand2", command=lambda:self.__save_to_json())
        self.add_program.image = img_add_program
        self.add_program.place(rely=0.35, relx=0.35)

        self.img_add_icon = PhotoImage(file="Assets/Images/image-gallery.png")
        self.add_program = tkinter.Button(self.middle_frame, text="Adicionar ícone", font=("Arial", 10, BOLD), image=self.img_add_icon, compound=LEFT, borderwidth=0, cursor="hand2", background="white", command=lambda:self.__upload_image())
        self.add_program.image = self.img_add_icon
        self.add_program.place(rely=0.6, relx=0.3)

    #Upload image
    def __upload_image(self):
        ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)
        
        filename = filedialog.askopenfilename()
        large, small = win32gui.ExtractIconEx(filename,0)
        win32gui.DestroyIcon(small[0])

        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_x)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0,0), large[0])
        hbmp.SaveBitmapFile( hdc, './assets/images/icon.png')

        self.img = Image.open('./assets/images/icon.png')
        self.img.thumbnail((26, 26))
        self.img.save(f'./assets/images/{self.__get_program_name()}.png')
        self.img_add_icon = ImageTk.PhotoImage(self.img)
        self.add_program.destroy()
        self.add_program = tkinter.Button(self.middle_frame, text="Adicionar ícone", font=("Arial", 10, BOLD), image=self.img_add_icon, compound=LEFT, borderwidth=0, cursor="hand2", background="white", command=lambda:self.__upload_image())
        self.add_program.image = self.img_add_icon
        self.add_program.place(rely=0.6, relx=0.3)

    #Return program name
    def __get_program_name(self):
        return self.program_name.get(1.0, "end-1c").replace(" ", "").lower()

    #Return extended program name (listed one)
    def __get_extended_program_name(self):
        return self.program_name.get(1.0, "end-1c")
    def __get_program_command(self):
        return self.program_command.get(1.0, "end-1c")

    #Save program to json
    def __save_to_json(self):
        new_program = {
            self.__get_program_name():{
                "nome": self.__get_extended_program_name(),
                "icone": f"./Assets/Images/{self.__get_program_name()}" + ".png",
                "comando": f"./Assets/Programs/{self.__get_program_command()}"
            }
        }
        self.json_file.data.update(new_program)
        print(self.json_file.data)
        with open('./Assets/Json/Programs.json', 'w') as f:
            json.dump(self.json_file.data, f)
        self.add_label['text'] = "Adicionado com sucesso!"
