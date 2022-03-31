from files_04_Wild_Farm.animals.animal import Mammal


class Mouse(Mammal):
    FOOD_TYPES = ['Vegetable', 'Fruit']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'

    def feed(self, food):
        if food.__class__.__name__ not in Mouse.FOOD_TYPES:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += food.quantity * 0.10
        self.food_eaten += food.quantity


class Dog(Mammal):
    FOOD_TYPES = ['Meat']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'

    def feed(self, food):
        if food.__class__.__name__ not in Dog.FOOD_TYPES:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity


class Cat(Mammal):
    FOOD_TYPES = ['Vegetable', 'Meat']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'

    def feed(self, food):
        if food.__class__.__name__ not in Cat.FOOD_TYPES:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity


class Tiger(Mammal):
    FOOD_TYPES = ['Meat']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food):
        if food.__class__.__name__ not in Tiger.FOOD_TYPES:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'

        self.weight += food.quantity * 1
        self.food_eaten += food.quantity

