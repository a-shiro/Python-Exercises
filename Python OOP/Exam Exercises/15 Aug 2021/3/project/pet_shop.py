class PetShop:
    def __init__(self, name: str): # test constructor 1 *
        self.name = name
        self.food = {}
        self.pets = []

    def add_food(self, name: str, quantity: float): # test add_food 4 *
        if quantity <= 0: # 2 (<, =)
            raise ValueError('Quantity cannot be equal to or less than 0')

        if name not in self.food: # 2 (with name in, without name in)
            self.food[name] = 0
        self.food[name] += quantity
        return f"Successfully added {quantity:.2f} grams of {name}."

    def add_pet(self, name: str): # test add_pet 2 *
        if name not in self.pets: # 1
            self.pets.append(name)
            return f"Successfully added {name}."
        raise Exception("Cannot add a pet with the same name") # 1

    def feed_pet(self, food_name: str, pet_name: str): # test feed_pet 4
        if pet_name not in self.pets: # 1
            raise Exception(f"Please insert a valid pet name")

        if food_name not in self.food: # 1
            return f'You do not have {food_name}'

        if self.food[food_name] < 100: # 1
            self.add_food(food_name, 1000.00)
            return "Adding food..."

        self.food[food_name] -= 100 # 1
        return f"{pet_name} was successfully fed"

    def __repr__(self): # test repr 1
        return f'Shop {self.name}:\n' \
               f'Pets: {", ".join(self.pets)}'
