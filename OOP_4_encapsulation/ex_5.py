class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def __setattr__(self, key, value):
        if key.startswith("a"):
            raise ValueError("invalid")
        self.__dict__[key] = value

    # def __getattr__(self, item):
    #     return None

    def get_id(self, pin):
        if self.__pin == pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old, new):
        if self.__pin == old:
            self.__pin = new
            return "Pin changed"
        return "Wrong pin"



account = Account(8827312, 100, 3421)
setattr(account, "dsa", "hello")
print(account.dsa)
del account.dsa
print(account.dsa)


