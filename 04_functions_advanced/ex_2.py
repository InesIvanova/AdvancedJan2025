def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


# data = {"name": "George", "town": "Sofia", "age": 20}
# print(get_info(data["name"], data["town"], data["age"]))
# print(get_info(**data))
# print(get_info(name=data["name"], town=data["town"], age=data["age"]))

print(get_info("Test", "Sofia", 40))
print(get_info(town="Sofia", name="Test", age=40))
print(get_info("Test", age=40, town="Sofia"))
