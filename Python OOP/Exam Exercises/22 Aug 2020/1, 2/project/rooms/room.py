from project import Appliance


class Room:
    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count

        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_cost = 0

        for list_of_obj in args:
            for obj in list_of_obj:
                if isinstance(obj, Appliance):
                    total_cost += obj.get_monthly_expense()
                else:
                    total_cost += obj.cost * 30

        self.expenses = total_cost


# laptop = Laptop()
# ch = Child(5, 5, 5)
# r = Room('Johnsons', 200, 3)
# r.calculate_expenses([laptop, ch])