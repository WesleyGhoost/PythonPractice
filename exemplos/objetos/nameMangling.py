#Diferença entre um underscore e dois underscores

class Example:
    def __init__(self):
        self._internal = 'Eu posso ser acessado fora da classe, embora não deva.'
        self.__private = 'Não é possivel me acessar diretamente fora da classe.'

obj = Example()
print(obj._internal)
#print(obj.__private): Retorna erro


#Name mangling é utilizado para que em um caso de herança, a classe filho não substitua métodos e atributos da classe pai
class Parent:
    def __init__(self):
        self.__data = 'Dados do pai'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Dados do filho'

c = Child()
print(c.__dict__)