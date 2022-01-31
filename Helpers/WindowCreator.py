import tkinter
from Pages.AddProgram import AddProgramPage
from Pages.Installer import InstallerPage
import json
from Helpers import ProgramsVariables

#Class that created and destroy windows
class WindowCreator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def on_closing(instance=None):
        list_selected = []
        for state in ProgramsVariables.ProgramsVariables.get_instance().programs_selected:
            list_selected.append(state.get())
        cache = {
            "programs":list_selected
        }
        with open('./Assets/Json/ProgramsCache.json', 'w') as f:
            json.dump(cache, f)
        if instance:
            instance.destroy()
        

    @staticmethod
    def access_add_program_page(instance):
        instance.destroy()
        root = tkinter.Tk()
        AddProgramPage.AddProgram(root)
        root.protocol("WM_DELETE_WINDOW", lambda:WindowCreator.on_closing(root))
        root.mainloop()

    @staticmethod
    def access_installer_page(instance):
        instance.destroy()
        root = tkinter.Tk()
        InstallerPage.Installer(root)
        root.protocol("WM_DELETE_WINDOW", lambda:WindowCreator.on_closing(root))
        root.mainloop()

    @staticmethod
    def exit_app(instance):
        WindowCreator.on_closing()
        instance.destroy()