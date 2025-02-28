class Profile:
    def __init__(self, username, password):
        # if len(username) < 5 or len(username) > 15:
        #     raise ValueError("can not accept that username")
        # else:
        #     self.username = username
        self.username = username

        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        # Or we can use this regex r"^(?=.*[A-Z])(?=.*\d).{8,}$"
        is_valid_length = len(value) >= 8
        is_capital_presented = len([c for c in value if c.isupper()]) >= 1
        is_digit_presented = len([c for c in value if c.isdigit()]) >= 1

        if not is_valid_length or not is_digit_presented or not is_capital_presented:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*"* len(self.__password)}'


p = Profile("asdasds", "asR5sdfsdfcsd")
p.username = "asd"
print(p.username)
