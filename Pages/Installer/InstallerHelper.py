import subprocess

#Class to help installer page
class Helper:

    def __init__(self, json_instance, programs_selected, page_instance):
        self.json_instance = json_instance
        self.programs_selected = programs_selected
        self.page_instance = page_instance
        self.commands_to_execute = []

    #Downloads the selected programs
    def download(self):
        i = 0
        while i < len(self.json_instance.json_keys):
            if self.get_button_status(i):
                print(self.json_instance.json_commands[i])
                self.commands_to_execute.append(self.json_instance.json_commands[i])
            i+=1
        
        if(len(self.commands_to_execute)):
            print("Existem processos!")
            self.progress_checker()
    
    #Get button status
    def get_button_status(self, key):
        return self.programs_selected.programs_selected[key].get()

    #Function to change progress label
    def progress_checker(self):
        self.page_instance.download_label['text'] = "Instalando Aplicativos..."
        self.process_checker()
        self.page_instance.download_label['text'] = "Aplicativos Instalados!"

    #Function to check the process
    def process_checker(self):
         bar_checker = 100/len(self.commands_to_execute)
         while(len(self.commands_to_execute) > 0):
             p = subprocess.Popen(self.__split_commands(self.commands_to_execute[0]))
             while(1):
                if p.poll() is not None:
                    self.commands_to_execute.pop()
                    self.page_instance.pb["value"] += bar_checker
                    break
                self.page_instance.pb.update()
    
    #Split executable commands            
    def __split_commands(self, command):
        commands_splitted = []
        commands_splitted = command.split(' ')
        return commands_splitted