class Walker:
    def walk(self):
        return 'Eu posso andar na terra'

class Swimmer:
    def swin(self):
        return 'eu posso nadar na água'

class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Eu sou {self.name}. {self.walk()} e {self.swin()}"

frog = Amphibian('Jack')
print(frog.introduce())