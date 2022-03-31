class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Ivan', 1000, 100)

    def test_worker_initialization(self):
        self.assertEqual('Ivan', self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)

    def test_worker_energy_goes_up_after_rest(self):
        self.worker.energy = 99
        self.worker.rest()
        self.assertEqual(100, self.worker.energy)

    def test_worker_tries_to_work_with_negative_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_money_increases_after_work(self):
        self.worker.salary = 100
        self.worker.work()
        self.assertEqual(100, self.worker.money)

    def test_worker_energy_decreases_after_work(self):
        self.worker.energy = 1
        self.worker.work()
        self.assertEqual(0, self.worker.energy)

    def test_get_info(self):
        info = self.worker.get_info()
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', info)


if __name__ == '__main__':
    unittest.main()