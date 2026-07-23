class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age= age
    def aowf(self):
        print(f"{self.name.upper()} says aowwf aowwf")

dog_one = Dog("Jack", 10)
dog_two = Dog("Mark", 8)

dog_one.aowf()
dog_two.aowf()


class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def describe(self):
        print(f"This is a {self.color} {self.model}")

car_1 = Car('Red', 'Toyota')
car_2 = Car('Blue', 'Fuska')

car_1.describe()
car_2.describe()


#metodos especiais
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        return self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} is not in the cart")

    def listItems(self):
        return self.items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

cart = Cart()

cart.add("Notebook")
cart.add("Celular")
cart.add("Abajur")
cart.add("Controle")

for item in cart:
    print(item)

cart.remove("Celular")

print(len(cart))
print("Celular" in cart)
print(list(cart))


#atributos dinamicos
class Person:
    pass

attributes_person = {
    "name": "Douglas",
    "age": 19,
    "gender": "Masculino",
    "weight": 68.5
}

person_1 = Person()

for attribute_name, attribute_value in attributes_person.items():
    setattr(person_1, attribute_name, attribute_value)

enter_attribute = input("Digite um dos atributos:")
print(getattr(person_1, enter_attribute, "Atributo não encontrado"))

attributes_to_remove = ['size', 'weight']

for attr in attributes_to_remove:
    if hasattr(person_1, attr):
        delattr(person_1, attr)
        print(f"Atributo: '{attr}' removido com sucesso.")