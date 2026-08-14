class Animal:
    def make_sound(self):
        print("Animal is making sound")
class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("bark")
a=Dog()
a.make_sound()