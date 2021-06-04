class Dog(object):
    pass


class Dog:
    def __init__(self, angry, count):
        self.angry = angry
        self.count = count

    def __repr__(self):
        return "Dog('" + self.angry + "', " + self.count + ")"

    def printer(self, angry, count):
        if angry:
            print(angry, count)
        else:
            print(angry)


my_dog = Dog(True, 6)
my_dog.printer(True, 666)