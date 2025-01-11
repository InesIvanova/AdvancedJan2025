n = int(input())

reservations = set()

for _ in range(n):
    reservation = input()
    reservations.add(reservation)

guest_reservation = input()
while guest_reservation != "END":
    reservations.remove(guest_reservation)
    guest_reservation = input()


all_VIP = [reservation for reservation in reservations if reservation[0].isdigit()]
all_regulars = [reservation for reservation in reservations if not reservation[0].isdigit()]

for guest in sorted(all_VIP ):
    print(guest)
for guest in sorted(all_regulars):
    print(guest)

print(len(reservations))
for guest in sorted(reservations):
    print(guest)