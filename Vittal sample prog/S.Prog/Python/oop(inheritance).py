class animal():
    def __init__(self):
        print("animal created")
    def who_am_i(self):
        print("i am an animal")
    def eat(self):
        print("i am eating")
myanimal = animal()

class dog(animal):
    def __init__(self):
        print("dog created")

mydog = dog()
