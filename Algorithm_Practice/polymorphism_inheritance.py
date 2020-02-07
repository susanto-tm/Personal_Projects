class Animal:
    def __init__(self, type):
        self.type = type

    def speak(self):
        print(f'I am {self.type}!!')


class Bird(Animal):
    def __init__(self, breed):
        super().__init__(breed)


class Dog(Animal):
    def __init__(self, breed):
        super().__init__(breed)


def main():
    b = Bird("Mocking Bird")
    d = Dog("Samoyed")

    b.speak()
    d.speak()


main()