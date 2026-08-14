class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def print_info(self):
        print(self.__name,self.__age)
    def set_name(self,name):
        self.__name=name

a=Student("arpitha",9)
a.set_name("arpithaaaaaaa")

a.age=100
a.print_info()