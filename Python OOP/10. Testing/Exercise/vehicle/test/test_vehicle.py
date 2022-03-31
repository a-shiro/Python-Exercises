from unittest import TestCase, main
from project import Vehicle


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(100, 200)

    def test_initializer(self):
        self.assertEqual(100, self.car.fuel)
        self.assertEqual(200, self.car.horse_power)
        self.assertEqual(100, self.car.capacity)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_class_returns_correct_string(self):
        result = str(self.car)

        self.assertEqual(f"The vehicle has {self.car.horse_power} "
                         f"horse power with {self.car.fuel} fuel left and "
                         f"{self.car.fuel_consumption} fuel consumption", result)

    def test_drive_with_less_than_the_needed_fuel_raises_error(self):
        with self.assertRaises(Exception) as cm:
            self.car.drive(100)
        self.assertEqual('Not enough fuel', str(cm.exception))

    def test_drive_with_enough_fuel_lowers_out_fuel_amount(self):
        self.car.drive(50)
        self.assertEqual(37.5, self.car.fuel)

    def test_refuel_with_more_fuel_than_we_can_hold(self):
        with self.assertRaises(Exception) as cm:
            self.car.refuel(120)
        self.assertEqual('Too much fuel', str(cm.exception))

    def test_refuel_increases_out_fuel_in_the_tank(self):
        self.car.fuel = 80
        self.car.refuel(20)

        self.assertEqual(100, self.car.fuel)


if __name__ == '__main__':
    main()