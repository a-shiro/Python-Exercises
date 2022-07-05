from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int): # only 2 tests?
        if len([car for car in self.cars if car.model == model]) == 1:
            raise Exception(f"Car {model} is already created!")

        car = self.__create_car_obj(car_type, model, speed_limit)
        if car is None:
            return

        self.cars.append(car)
        return f"{car_type} {model} is created."

    @staticmethod
    def __create_car_obj(car_type, model, speed_limit):
        if car_type == 'MuscleCar':
            return MuscleCar(model, speed_limit)
        if car_type == 'SportsCar':
            return SportsCar(model, speed_limit)

    def create_driver(self, driver_name: str):
        if len([driver for driver in self.drivers if driver.name == driver_name]) == 1:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if len([race for race in self.races if race.name == race_name]) == 1:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if len([driver for driver in self.drivers if driver.name == driver_name]) == 0:
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [driver for driver in self.drivers if driver.name == driver_name][0]
        car = self.__find_car(car_type)

        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_model = driver.car.model
            driver.car.is_taken = False

            driver.car = car
            driver.car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f'Driver {driver_name} chose the car {car.model}.'

    def __find_car(self, car_type):
        for car in list(reversed(self.cars)):
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        return None

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if len([race for race in self.races if race.name == race_name]) == 0:
            raise Exception(f"Race {race_name} could not be found!")

        if len([driver for driver in self.drivers if driver.name == driver_name]) == 0:
            raise Exception(f"Driver {driver_name} could not be found!")

        race = [race for race in self.races if race.name == race_name][0]
        driver = [driver for driver in self.drivers if driver.name == driver_name][0]

        if len([driver for driver in race.drivers if driver.name == driver_name]) == 1:
            return f"Driver {driver_name} is already added in {race_name} race."

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        race.drivers.append(driver)
        return f'Driver {driver_name} added in {race_name} race.'

    def start_race(self, race_name: str):
        if len([race for race in self.races if race.name == race_name]) == 0:
            raise Exception(f"Race {race_name} could not be found!")

        race = [race for race in self.races if race.name == race_name][0]

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        first_3 = list(sorted(race.drivers, key=lambda x: x.car, reverse=True))[0:3]

        result = ''
        for driver in first_3:
            driver.number_of_wins += 1
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"

        return result.strip()