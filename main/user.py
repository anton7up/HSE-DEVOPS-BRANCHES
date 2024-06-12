class User:

    def __init__(self, username, name, lastname, login, password):
        self.username = username
        self.name = name
        self.lastname = lastname
        self._login = login
        self.__password = password

    def get_username(self):
        return self.username

    def change_password(self, new_password):
        self.__password = new_password
