class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print(f" student name:{self.name} \n student marks:{self.marks}")
s1=Student("arpitha",20)
s2=Student("chandan",29)
s1.display_info()