from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


def create_food(food_type, name, price):
    if food_type == 'Bread':
        return Bread(name, price)

    if food_type == 'Cake':
        return Cake(name, price)


def create_drink(drink_type, name, portion, brand):
    if drink_type == 'Tea':
        return Tea(name, portion, brand)

    if drink_type == 'Water':
        return Water(name, portion, brand)


def create_table(table_type, table_number, capacity):
    if table_type == 'InsideTable':
        return InsideTable(table_number, capacity)

    if table_type == 'OutsideTable':
        return OutsideTable(table_number, capacity)


def get_first_available_table(number_of_people, table_repository):
    for table in table_repository:
        if table.capacity >= number_of_people and not table.is_reserved:
            return table
    return None


class Bakery:
    def __init__(self, name):
        self.name = name

        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []

        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        available_food = [food.name for food in self.food_menu]
        food = create_food(food_type, name, price)

        if food.name in available_food:
            raise Exception(f'{food_type} {name} is already in the menu!')

        self.food_menu.append(food)
        return f'Added {name} ({food_type}) to the food menu'

    def add_drink(self, drink_type, name, portion, brand):
        available_drinks = [drink.name for drink in self.drinks_menu]
        drink = create_drink(drink_type, name, portion, brand)

        if drink.name in available_drinks:
            raise Exception(f'{drink_type} {name} is already in the menu!')

        self.drinks_menu.append(drink)
        return f'Added {name} ({brand}) to the drink menu'

    def add_table(self, table_type, table_number, capacity):
        available_table_numbers = [table.table_number for table in self.tables_repository]
        table = create_table(table_type, table_number, capacity)

        if table.table_number in available_table_numbers:
            raise Exception(f'Table {table_number} is already in the bakery!')

        self.tables_repository.append(table)
        return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people):
        table = get_first_available_table(number_of_people, self.tables_repository)

        if table is None:
            return f'No available table for {number_of_people} people'

        table.reserve(number_of_people)
        return f'Table {table.table_number} has been reserved for {number_of_people} people'

    def order_food(self, table_number, *args):
        table = [table if table.table_number == table_number else None for table in self.tables_repository][0]

        if table is None:
            return f'Could not find table {table_number}'

        available_foods = [food.name for food in self.food_menu]

        available_orders = []
        unavailable_orders = []


        [available_orders.append(self.__get_order(order)) if order in available_foods else unavailable_orders.append(order) for order in args]
        [table.order_food(food) for food in available_orders]

    def order_drink(self, table_number, *args):
        pass

    def leave_table(self, table_number):
        pass

    def get_free_tables_info(self):
        pass

    def get_total_income(self):
        pass

    def __get_order(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food
