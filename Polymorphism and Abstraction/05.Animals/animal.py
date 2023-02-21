from abc import ABC,abstractmethod


class Animal(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass
