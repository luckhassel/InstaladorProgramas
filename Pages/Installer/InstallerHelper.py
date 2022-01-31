import subprocess
import os
import threading

#Class to help installer page
class Helper:

    def __init__(self, json_instance, programs_selected, page_instance):
        self.json_instance = json_instance
        self.programs_selected = programs_selected
        self.page_instance = page_instance
        self.commands_to_execute = []
        self.programs_to_execute = []
        self.select_deselect_all = 0
        self.select_deselect_basic = 0
        self.select_deselect_essential = 0

    #Downloads the selected programs
    def download(self):
        i = 0
        while i < len(self.json_instance.json_keys):
            if self.get_button_status(i):
                print(self.json_instance.json_commands[i])
                self.commands_to_execute.append(self.json_instance.json_commands[i])
                self.programs_to_execute.append(self.json_instance.json_names[i])
            i+=1
        
        if(len(self.commands_to_execute)):
            print("Existem processos!")
            self.update_label()
    
    #Get button status
    def get_button_status(self, key):
        return self.programs_selected.programs_selected[key].get()

    #Function to change progress label
    def update_label(self):
        self.process_checker()
        self.page_instance.download_label['text'] = "Aplicativos Instalados!"

    #Function to check the process
    def process_checker(self):
         bar_checker = 100/len(self.commands_to_execute)
         self.page_instance.pb["value"] = 0
         self.page_instance.pb.update()
         while(len(self.commands_to_execute) > 0):
            self.page_instance.download_label['text'] = f"Instalando {self.programs_to_execute[0]}..."
            self.page_instance.pb.update()
            threading.Thread(target=os.system(self.commands_to_execute[0]))
            self.page_instance.pb["value"] += bar_checker
            del self.commands_to_execute[0]
            del self.programs_to_execute[0]
            self.page_instance.pb.update()
    
    #Split executable commands            
    def __split_commands(self, command):
        commands_splitted = []
        commands_splitted = command.split(' ')
        return commands_splitted

    def install_all_programs(self):
        i=0
        self.select_deselect_all += 1
        while i < len(self.programs_selected.programs_selected):
            if self.select_deselect_all % 2 == 0:
                self.programs_selected.programs_selected[i].set(0)
            else:
                self.programs_selected.programs_selected[i].set(1)
            i += 1
    
    def install_basic_programs(self):
        i=0
        self.select_deselect_basic += 1
        while i < len(self.json_instance.data):
            if(self.json_instance.json_keys[i] in self.programs_selected.basic_programs):
                if self.select_deselect_basic % 2 == 0:
                    self.programs_selected.programs_selected[i].set(0)
                else:
                    self.programs_selected.programs_selected[i].set(1)
            i += 1

    def install_essential_programs(self):
        i=0
        self.select_deselect_essential += 1
        while i < len(self.json_instance.data):
            if(self.json_instance.json_keys[i] in self.programs_selected.essential_programs):
                    if self.select_deselect_essential % 2 == 0:
                        self.programs_selected.programs_selected[i].set(0)
                    else:
                        self.programs_selected.programs_selected[i].set(1)
            i += 1