class Trainer:

    _counter = 0

    def __init__(self, name):
        Trainer._counter += 1
        self.name = name
        self.id = Trainer._counter

    @staticmethod
    def get_next_id():
        return Trainer._counter + 1

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
