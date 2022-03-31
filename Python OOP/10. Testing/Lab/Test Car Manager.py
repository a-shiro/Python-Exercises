class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class TestCarManager(TestCase):
    def setUp(self) -> None:
        self.car = Car('VW', 'Porsche', 5, 20)

    def test_manufacturer(self):
        self.assertEqual('VW', self.car.make)

    def test_car_doesnt_have_a_manufacturer_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_model(self):
        self.assertEqual('Porsche', self.car.model)

    def test_car_doesnt_have_a_model_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_fuel_consumption(self):
        self.assertEqual(5, self.car.fuel_consumption)

    def test_given_negative_fuel_consumption_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_fuel_capacity(self):
        self.assertEqual(20, self.car.fuel_capacity)

    def test_given_negative_fuel_capacity_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_fuel_amount(self):
        self.assertEqual(0, self.car.fuel_amount)

    def test_given_negative_fuel_amount_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_refuel(self):
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_with_more_than_capacity(self):
        self.car.refuel(50)
        self.assertEqual(20, self.car.fuel_amount)

    def test_given_negative_fuel_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-20)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_drive(self):
        self.car.fuel_amount = 20
        self.car.drive(1)
        self.assertEqual(19.95, self.car.fuel_amount)

    def test_drive_with_no_fuel(self):
        self.car.fuel_amount = 0
        with self.assertRaises(Exception) as ex:
            self.car.drive(20)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_if_not_enough_fuel(self):
        self.car.fuel_amount = 5
        with self.assertRaises(Exception) as ex:
            self.car.drive(200)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()