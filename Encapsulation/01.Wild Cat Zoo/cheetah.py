from project.animal import Animal


class Cheetah(Animal):
    def __init__(self, name, age, gender, money_for_care=0):
        super().__init__(name, age, gender, money_for_care)
        self.money_for_care = 60