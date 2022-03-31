class Pokemon:
    def __init__(self, pokemon_name, health):
        self.pokemon_name = pokemon_name
        self.health = health

    def pokemon_details(self):
        return f'{self.pokemon_name} with health {self.health}'
