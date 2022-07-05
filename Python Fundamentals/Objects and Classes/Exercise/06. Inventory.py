class Inventory:
    def __init__(self, capacity):
        self.__starting_capacity = capacity
        self.__capacity = capacity
        self.items = []

    def get_capacity(self):
        return self.__starting_capacity

    def add_item(self, item):
        if self.__capacity == 0:
            return 'not enough room in the inventory'

        self.items.append(item)
        self.__capacity -= 1

    def __repr__(self):
        return f'Items: {", ".join(self.items)}.\nCapacity left: {self.__capacity}'


inventory = Inventory(2)
inventory.add_item('potion')
inventory.add_item('sword')
print(inventory.add_item('bottle'))
print(inventory.get_capacity())
print(inventory)