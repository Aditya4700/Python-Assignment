class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def type(self):
        pass


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cow")

    def type(self):
        return "Domestic"

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name, species="Horse")

    def type(self):
        return "Domestic"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="Dog")

    def type(self):
        return "Pet"

