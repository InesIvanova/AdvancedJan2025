from collections import deque

name = input()
customers = deque()

while name != "End":
    if name == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(name)
    name = input()

print(f"{len(customers)} people remaining.")
