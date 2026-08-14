class Animal:
    def make_sound(self):
        print("animal is making sound")
class Dog(Animal):
    def make_sound(self):
        print("bark")
class cat(Animal):
    def make_sound(self):
        print("meow")
animals=[Dog(),cat()]
for animal in animals:
    animal.make_sound()