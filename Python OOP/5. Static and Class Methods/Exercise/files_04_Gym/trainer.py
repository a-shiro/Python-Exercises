class Trainer:
    id = 1

    def __init__(self, name):
        self.id = Trainer.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        current_id = Trainer.id
        Trainer.id += 1
        return current_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
