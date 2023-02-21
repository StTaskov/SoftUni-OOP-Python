class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.len_password(value) and self.one_capital_letter(value) and self.one_digit(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def len_password(self, value):
        if len(value) >= 8:
            return True
        return False

    def one_capital_letter(self, value):
        letters = [el for el in value if el.isupper()]
        if letters:
            return True
        return False

    def one_digit(self, value):
        digits = [el for el in value if el.isdigit()]
        if digits:
            return True
        return False

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
