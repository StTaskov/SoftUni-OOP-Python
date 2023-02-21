from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):

        fuel = self.fuel_consumption + 0.9
        if self.fuel_quantity > distance * fuel:
            self.fuel_quantity -= distance * fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):

        self.fuel_consumption += 1.6

        if self.fuel_quantity > distance * self.fuel_consumption:
            self.fuel_quantity -= distance * self.fuel_consumption

    def refuel(self, fuel):

        the_fuel_which_can_receive = 95/100 * fuel

        self.fuel_quantity += the_fuel_which_can_receive