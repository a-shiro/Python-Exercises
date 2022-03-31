from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


def create_astronaut(astronaut_type, name):
    if astronaut_type == 'Biologist':
        return Biologist(name)

    if astronaut_type == 'Geodesist':
        return Geodesist(name)

    if astronaut_type == 'Meteorologist':
        return Meteorologist(name)

    raise Exception("Astronaut type is not valid!")


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

        self.successful_missions = 0
        self.unsuccessful_mission = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f'{name} is already added.'

        astronaut = create_astronaut(astronaut_type, name)

        self.astronaut_repository.add(astronaut)
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)

        if planet is None:
            raise Exception("Invalid planet name!")

        astronauts = self.astronaut_repository.find_suited_astronauts()

        if len(astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        participants = 0

        for astronaut in astronauts:
            if len(planet.items) == 0:
                break
            participants += 1
            while len(planet.items) > 0 and astronaut.oxygen > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

        if planet.items:
            self.unsuccessful_mission += 1
            return "Mission is not completed."

        self.successful_missions += 1
        return f"Planet: {planet_name} was explored. {participants} astronauts participated in collecting items."

    def report(self):
        result = f'{self.successful_missions} successful missions!\n' +\
                 f'{self.unsuccessful_mission} missions were not completed!\n' +\
                 f"Astronauts' info:\n"

        for astronaut in self.astronaut_repository.astronauts:
            result += f'Name: {astronaut.name}\n' +\
                      f'Oxygen: {astronaut.oxygen}\n' +\
                      f'Backpack items: {", ".join(astronaut.backpack) if astronaut.backpack else "none"}\n'

        return result.strip()
