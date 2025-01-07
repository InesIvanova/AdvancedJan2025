from collections import deque

liters = int(input())

people = deque()

name = input()

while name != "Start":
    people.append(name)
    name = input()

command = input()
while command != "End":
    if "refill" in command:
        _, liters_to_refill = command.split()
        liters_to_refill = int(liters_to_refill)
        liters += liters_to_refill
    else:
        liters_requested = int(command)
        name = people.popleft()
        if liters_requested <= liters:
            liters -= liters_requested
            print(f"{name} got water")
        else:
            print(f"{name} must wait")

    command = input()

print(f"{liters} liters left")
