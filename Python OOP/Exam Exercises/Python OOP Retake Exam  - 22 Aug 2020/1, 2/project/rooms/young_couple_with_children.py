from project import Fridge
from project import Laptop
from project import TV
from project import Room


def get_appliances(children):
    result = []

    for _ in range(len(children) + 2):
        result.append(TV())
        result.append(Fridge())
        result.append(Laptop())

    return result


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, len(children) + 2)
        self.room_cost = 30
        self.children = [child for child in children]
        self.appliances = get_appliances(self.children)
        self.calculate_expenses(self.children, self.appliances)
