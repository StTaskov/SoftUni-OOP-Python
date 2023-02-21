class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):

        dvd_names = [dvd.name for dvd in self.rented_dvds]

        return f"{self.id}: {self.name} of age {self.age} has {len(dvd_names)} " \
               f"rented DVD's ({', '.join(dvd_names)})"
