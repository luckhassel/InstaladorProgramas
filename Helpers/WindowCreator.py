import tkinter
from Pages.AddProgram import AddProgramPage
from Pages.Installer import InstallerPage

#Class that created and destroy windows
class WindowCreator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def access_add_program_page(instance):
        instance.destroy()
        root = tkinter.Tk()
        AddProgramPage.AddProgram(root)
        root.mainloop()

    @staticmethod
    def access_installer_page(instance):
        instance.destroy()
        root = tkinter.Tk()
        InstallerPage.Installer(root)
        root.mainloop()

    @staticmethod
    def exit_app(instance):
        instance.destroy()