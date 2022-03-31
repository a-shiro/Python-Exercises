# Original Code:

# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)


# Refactored Code:

from abc import ABC, abstractmethod


class SpeciesIdentifier:
    @staticmethod
    def identify(animal):
        return animal.species


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return 'meow'


class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'


animals = [Cat('cat'), Dog('dog')]
identifier = SpeciesIdentifier()

for animal in animals:
    print(f'Species: {identifier.identify(animal)}, Sound: {animal.make_sound()}')


