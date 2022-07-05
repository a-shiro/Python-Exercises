from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name, 25)

    def add_fish(self, fish):
        if self.capacity == len(self.fish):
            return 'Not enough capacity.'

        if not fish.__class__.__name__ == 'SaltwaterFish':
            return 'Water not suitable.'

        self.fish.append(fish)
        return f'Successfully added {fish.__class__.__name__} to {self.name}.'