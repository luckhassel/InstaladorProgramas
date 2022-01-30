
#Singleton class to store user name
class UserData:
    __instance = None

    @staticmethod
    def get_instance():
        return UserData.__instance

    def __init__(self):
        UserData.__instance = self
        self.user_name = None

    def set_user_name(self, name):
        self.user_name = name