from tkinter import *
import tkinter
from Pages.Installer.InstallerPage import Installer
from Pages.AddProgram import AddProgramPage

#Creates an instance and start the app
def main():
    root = tkinter.Tk()
    app = Installer(root)
    root.mainloop()

if __name__ == '__main__':
    main()