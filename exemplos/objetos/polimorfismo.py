class Dog:
    def speak(self):
        return 'Cachorro faz roowf roowf'

class Cat:
    def speak(self):
        return 'Gato faz miau'

class Cow:
    def speak(self):
        return 'Vaca faz muuuuu'

#def animal_sound(animal):
    #print(animal.speak())

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.speak())