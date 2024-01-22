class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("this method is not implemented yet!")


class Dog(Animal):
    def sound(self):
        return "woof"


dog1 = Dog("mamuka")
print(dog1.sound())
