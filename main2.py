class Account:
    def __init__(self, number, email):
        self.number = number
        self.__email = email
        self.__id = "asd"

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if len(new_email) < 5:
            raise ValueError("Length must be above 5")
        domain = new_email.split("@")[-1]
        if domain != "softuni.bg":
            raise ValueError("We are working only with internal emails, this email is not part of the organization")
        self.__email  = new_email
        # return self.__email[0] + "****" + self.__email[-1]

    def get_id(self):
        return self.__id


a = Account("12333", "example@exam.com")
try:
    a.set_email("ines@softuni.bg")
except ValueError as ex:
    print(str(ex))
print(a.get_email())


