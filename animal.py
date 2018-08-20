from abc import ABC,abstractmethod

class Abstractanimal(ABC):
    @abstractmethod
    def bark(self):pass

class Dog(Abstractanimal):
    def bark(self):
        print("bow bow")

print(Dog.bark())