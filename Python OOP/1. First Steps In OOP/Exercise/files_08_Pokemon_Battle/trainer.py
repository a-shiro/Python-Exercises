class Trainer:
    def __init__(self, name):
        self.name = name
        self.collection = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.collection:
            self.collection.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        return 'This pokemon is already caught'

    def release_pokemon(self, pokemon_name):
        for el in self.collection:
            if el.pokemon_name == pokemon_name:
                self.collection.remove(el)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\nPokemon count {len(self.collection)}'
        for p in self.collection:
            result += f'\n'
            result += f'- {p.pokemon_details()}'

        return result

