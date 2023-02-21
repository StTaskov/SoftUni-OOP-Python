class Customer:
    _counter = 0

    def __init__(self, name, address, email):
        Customer._counter += 1
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer._counter

    @staticmethod
    def get_next_id():
        return Customer._counter + 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
