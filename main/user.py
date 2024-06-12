import re
class User:

    def is_valid_email(self, email):
        regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
        if re.match(regex, email):
            return True
        else:
            return False

    def is_strong_password(self, password):
        if len(password) < 8:
            return False
        if not re.search(r"[a-z]", password) and not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if re.search(r"(.)\1\1", password):
            return False
        return True

    def __init__(self, username, name, lastname, login, password):
        self.username = username
        self.name = name
        self.lastname = lastname
        # проверка корректности введенной почты
        if self.is_valid_email(login):
            self._login = login
        else:
            raise ValueError
        # проверка надежного пароля
        if self.is_strong_password(password):
            self.__password = password
        else:
            raise ValueError

    def get_username(self):
        return self.username

    def change_password(self, new_password):
        self.__password = new_password
