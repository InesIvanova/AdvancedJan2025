n = int(input())
parking = set()

for _ in range(n):
    direction, car_number = input().split(", ")

    if direction == "IN":
        parking.add(car_number)
    elif direction == "OUT":
        if car_number not in parking:
            continue
        parking.remove(car_number)

if len(parking) == 0:
    print("Parking Lot is Empty")
else:
    for el in parking:
        print(el)
    print("\n".join(parking))

