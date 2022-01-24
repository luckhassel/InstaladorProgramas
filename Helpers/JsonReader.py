import json

class JsonHelper:

    def __init__(self):
        self.json_file = open("Assets/Json/Programs.json")
        self.data = json.load(self.json_file)
        self.json_keys = []
        self.json_icons = []
        self.json_names = []
        self.json_commands = []
        self.json_status = []
        self.__get_keys()
        self.__get_names()
        self.__get_icons()
        self.__get_commands()

    def __get_keys(self):
        for key in self.data.keys():
            self.json_keys.append(key)

    def __get_names(self):
        for key in self.json_keys:
            self.json_names.append(self.data[key]["nome"])

    def __get_icons(self):
        for key in self.json_keys:
            self.json_icons.append(self.data[key]["icone"])

    def __get_commands(self):
        for key in self.json_keys:
            self.json_commands.append(self.data[key]["comando"])

    def __get_status(self):
        for key in self.json_keys:
            self.json_status.append(self.data[key]["status"])