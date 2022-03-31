from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name:str):
        aquarium = self.__create_aquarium(aquarium_type, aquarium_name)

        if aquarium is None:
            return f'Invalid aquarium type.'

        self.aquariums.append(aquarium)
        return f'Successfully added {aquarium_type}.'

    @staticmethod
    def __create_aquarium(aquarium_type, aquarium_name):
        if aquarium_type == 'FreshwaterAquarium':
            return FreshwaterAquarium(aquarium_name)
        if aquarium_type == 'SaltwaterAquarium':
            return SaltwaterAquarium(aquarium_name)
        return None

    def add_decoration(self, decoration_type: str):
        decoration = self.__create_decoration(decoration_type)

        if decoration is None:
            return 'Invalid decoration type.'

        self.decorations_repository.add(decoration)
        return f'Successfully added {decoration_type}.'

    @staticmethod
    def __create_decoration(decoration_type):
        if decoration_type == 'Ornament':
            return Ornament()
        if decoration_type == 'Plant':
            return Plant()
        return None

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration is None:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.__find_aquarium(aquarium_name)

        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = self.__create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.__find_aquarium(aquarium_name)

        if fish is None:
            return f"There isn't a fish of type {fish_type}."

        return aquarium.add_fish(fish)

    @staticmethod
    def __create_fish(fish_type, fish_name, fish_species, price):
        if fish_type == 'FreshwaterFish':
            return FreshwaterFish(fish_name, fish_species, price)
        if fish_type == 'SaltwaterFish':
            return SaltwaterFish(fish_name, fish_species, price)
        return None

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)

        aquarium.feed()
        return f'Fish fed: {len(aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)

        total_value = sum(x.price for x in aquarium.fish + aquarium.decorations)
        return f'The value of Aquarium {aquarium_name} is {total_value:.2f}.'

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium)
        return result.strip()

    def __find_aquarium(self, aquarium_name):
        return [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]