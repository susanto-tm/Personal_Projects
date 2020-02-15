class Animal:
    def __init__(self, type):
        self.type = type
        self._breed = type

    def speak(self):
        print(f'I am {self._breed}!!')

    __speak = speak


class Bird(Animal):
    def __init__(self, breed):
        super().__init__(breed)

    def speak(self):
        print(self._breed)


class Dog(Animal):
    def __init__(self, breed):
        super().__init__(breed)


def main():
    b = Bird("Mocking Bird")
    d = Dog("Samoyed")

    b.speak()
    d.speak()


main()