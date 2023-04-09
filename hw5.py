class Dog:
    biology_class = 'Animal'

    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def run(self):
        return 'I can run'

    def get_name(self):
        return f'Hello! My name is {self.name}'

    def set_name(self, new_name):
        self.name = new_name


dog1 = Dog('Rex', 3, 'brown')
print(dog1.name)
print(dog1.get_name())


class Buldog(Dog):

    def __init__(self, name, weight, color, _passport):
        super().__init__(name, weight, color)
        self._passport = _passport

    def get_passport(self):
        return f'Passport is {self._passport}'

    def set_passport(self, new_passport):
        self._passport = new_passport


dog2 = Buldog('Bob', 2, 'black', 'type1')
print(dog2.get_passport())
print(dog2.biology_class)
dog2.set_passport('type2')
print(dog2.get_passport())
