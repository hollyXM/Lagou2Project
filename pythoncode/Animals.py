class Animal(object):
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def canRun(self):
        print("I can run~")

    def canCry(self):
        print("I can cry~")


class Cat(Animal):
    hair = "short"

    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)

    def catchMouse(self):
        print("I can catch mouse")
        return ("I did catch a mouse")

    def canCry(self):
        print("miao~miao~")


class Dog(Animal):
    hair = "long"

    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)

    def guardHouse(self):
        print("I can guard house")
        return ("I did guard a house")

    def canCry(self):
        print("wang~wang~")


def main():
    myCat = Cat("mimi", "white", "7", "female")
    resultOfCatchMouse = myCat.catchMouse()
    print('%s,%s,%s,%s,%s,%s' % (myCat.name, myCat.color, myCat.age, myCat.gender, myCat.hair, resultOfCatchMouse))

    myDog = Dog("wangcai", "black", "11", "male")
    resultOfGuardHouse = myDog.guardHouse()
    print('%s,%s,%s,%s,%s,%s' % (myDog.name, myDog.color, myDog.age, myDog.gender, myDog.hair, resultOfGuardHouse))


if __name__ == '__main__':
    main()
