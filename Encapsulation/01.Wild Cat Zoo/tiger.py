from project.animal import Animal


class Tiger(Animal):
    def __init__(self, age, name, gender, money_for_care=0):
        super().__init__(age, name, gender, money_for_care)
        self.money_for_care = 45
