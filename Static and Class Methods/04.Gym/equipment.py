import itertools


class Equipment:
    _counter = 0

    def __init__(self, name):
        Equipment._counter += 1
        self.name = name
        self.id = Equipment._counter

    @staticmethod
    def get_next_id():
        return Equipment._counter + 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
