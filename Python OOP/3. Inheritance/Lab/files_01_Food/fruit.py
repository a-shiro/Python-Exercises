from files_01_Food.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        self.name = name
        super().__init__(expiration_date)

