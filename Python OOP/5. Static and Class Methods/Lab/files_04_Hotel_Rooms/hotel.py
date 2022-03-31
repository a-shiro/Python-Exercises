from files_04_Hotel_Rooms.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, starts_count):
        return cls(f'{starts_count} stars Hotel')  # this should not be the hotel name

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):  # here it matters if the room cannot be taken because we shouldn't add
        for room in self.rooms:                # guests to the hotel total if it is taken
            if room.number == room_number:
                guests_not_accommodated = room.take_room(people)

                if guests_not_accommodated:
                    return
                self.guests += people

    def free_room(self, room_number):  # here it doesn't matter if the room is free because if so room.guests == 0
        for room in self.rooms:        # and self.guests -= room.guests doesn't change anything
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()

    def status(self):
        free_rooms = [r for r in self.rooms if not r.is_taken]
        taken_rooms = [r for r in self.rooms if r.is_taken]

        result = f"Hotel {self.name} has {self.guests} total guests" + '\n' + \
                 f"Free rooms: {', '.join([str(r.number) for r in free_rooms])}" + '\n' + \
                 f"Taken rooms: {', '.join([str(r.number) for r in taken_rooms])}"
        return result