from files_04_Wild_Farm.animals.animal import Bird


class Owl(Bird):
    FOOD_TYPES = ['Meat']

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food):
        if food.__class__.__name__ not in Owl.FOOD_TYPES:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):
    FOOD_TYPES = ['Meat', 'Vegetable', 'Fruit', 'Seed']

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'

    def feed(self, food):
        if food.__class__.__name__ not in Hen.FOOD_TYPES:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity