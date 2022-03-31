class Equipment:
    id = 1

    def __init__(self, name):
        self.id = Equipment.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        current_id = Equipment.id
        Equipment.id += 1
        return current_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"