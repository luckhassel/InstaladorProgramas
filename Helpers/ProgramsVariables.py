from Helpers import JsonReader

class ProgramsVariables:

    __instance = None

    @staticmethod
    def get_instance():
        return ProgramsVariables.__instance

    #Define number of programs
    def __init__(self, programs_size):
        ProgramsVariables.__instance = self
        if(JsonReader.JsonHelper.has_cache()):
            self.programs_selected = JsonReader.JsonHelper.get_pattern()
        else:
            self.programs_selected = [0]*programs_size
        self.basic_programs = ["adobe", "anydesk"]
        self.essential_programs = ["adobe", "javase6", "firefox"]