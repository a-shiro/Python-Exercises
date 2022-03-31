from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    @abstractmethod
    def add_fish(self, fish):
        pass

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat() for fish in self.fish]

    def __str__(self):
        fish_names = [fish.name for fish in self.fish]

        result = f'{self.name}:\n' +\
                 f'Fish: {"none" if len(fish_names) == 0 else " ".join(fish_names)}\n' +\
                 f'Decorations: {len(self.decorations)}\n' +\
                 f'Comfort: {self.calculate_comfort()}\n'

        return result
