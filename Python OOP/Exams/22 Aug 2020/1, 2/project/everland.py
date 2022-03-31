class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_expenses = 0
        for room in self.rooms:
            total_expenses += room.expenses + room.room_cost

        return f'Monthly consumtions: {total_expenses:.2f}$. ' ### ??????? consumtion?? and space at the end?

    def pay(self):
        result = ''
        for room in self.rooms:
            if room.budget >= room.expenses:
                result += f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget - (room.expenses + room.room_cost):.2f}$ left.\n"
                room.budget -= room.expenses + room.room_cost
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)

        return result.strip()

    def status(self):
        total_population = sum([room.members_count for room in self.rooms])

        result = f'Total population: {total_population}\n'

        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'

            for idx, child in enumerate(room.children):
                result += f'--- Child {idx + 1} monthly cost: {child.cost * 30:.2f}$\n'

            result += f'--- Appliances monthly cost: {sum([appliance.get_monthly_expense() for appliance in room.appliances]):.2f}$\n'

        return result.strip()