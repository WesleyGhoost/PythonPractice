from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print('Meow meow')

class Dog(Animal):
    def make_sound(self):
        print('ouf ouf')

animals = [Cat(), Dog()]

for animal in animals:
    animal.make_sound()
