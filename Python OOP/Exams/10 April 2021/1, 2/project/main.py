from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller

controller = Controller()

print(controller.add_aquarium('SaltwaterAquarium', 'A2'))
print(controller.add_aquarium('SaltwaterAquarium', 'A3'))
print(controller.add_fish('A2', 'SaltwaterFish', 'jeff', 'tuna', 3))
print(controller.add_decoration('Plant'))
print(controller.insert_decoration('A2', 'Plant'))
print(controller.report())