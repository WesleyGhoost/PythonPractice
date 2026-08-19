class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('radius must be positive')
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

my_circle = Circle(3)
print(my_circle.radius)

my_circle.radius = 10
print(my_circle.radius)

del my_circle.radius

try:
    print(my_circle.radius)
except AttributeError as error:
    print(f'Erro: {error}')