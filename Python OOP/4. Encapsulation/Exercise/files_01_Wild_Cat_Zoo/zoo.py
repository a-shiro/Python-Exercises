class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return 'Not enough budget'

        if self.__animal_capacity == 0:
            return 'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price
        self.__animal_capacity -= 1
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_to_be_paid = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_to_be_paid:
            self.__budget -= total_to_be_paid
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_animal_care_fees = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_animal_care_fees:
            self.__budget -= total_animal_care_fees
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animal_types = {
            'Lion': 0,
            'Tiger': 0,
            'Cheetah': 0
        }

        for animal in self.animals:
            animal_types[type(animal).__name__] += 1

        result = f'You have {len(self.animals)} animals'

        for k, v in animal_types.items():
            result += '\n'
            result += f'----- {v} {k}s:'
            for animal in self.animals:
                if type(animal).__name__ == k:
                    result += '\n'
                    result += f'{animal}'
        return result

    def workers_status(self):
        worker_types = {
            'Keeper': 0,
            'Caretaker': 0,
            'Vet': 0
        }

        for worker in self.workers:
            worker_types[type(worker).__name__] += 1

        result = f'You have {len(self.workers)} workers'

        for k, v in worker_types.items():
            result += '\n'
            result += f'----- {v} {k}s:'
            for worker in self.workers:
                if type(worker).__name__ == k:
                    result += '\n'
                    result += f'{worker}'
        return result
