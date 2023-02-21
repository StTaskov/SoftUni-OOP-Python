class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        amount = self.quantity + milliliters
        if amount < self.size:
            self.quantity += milliliters

    def status(self):
        status = self.size - self.quantity
        return status


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

