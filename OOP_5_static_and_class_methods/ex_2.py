class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        self.__is_small = False

    @classmethod
    def small_shop(cls, name, type):
        shop = cls(name, type, 10)
        shop.__is_small = True
        return shop

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if hasattr(self, "_Shop__is_small") and self.__is_small:
            raise ValueError("Capacity can not be changed for small shops")
        self.__capacity = value

    def add_item(self, item_name):
        if self.capacity == sum(self.items.values()):
            return "Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] +=1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name:str, amount:int):
        if item_name not in self.items:
            return f"Cannot remove {amount} {item_name}"
        if self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            del self.items[item_name]

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


# s = Shop.small_shop("test", "vegies")
# s.capacity = 40

s2 = Shop("asd", "fruits", 50)
s2.capacity = 30
print(s2.capacity)