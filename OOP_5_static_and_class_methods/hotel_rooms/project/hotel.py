from project.room import Room

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms: list[Room] = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self):
        free_room_numbers = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_room_numbers = [str(r.number) for r in self.rooms if r.is_taken]
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(free_room_numbers)}\n"
                f"Taken rooms: {', '.join(taken_room_numbers)}")


