def decorator_name(func):
    def wrapper():
        print("helllo,good morning")
        func()
        print("good byee")
    return wrapper
@decorator_name
def into():
    print("hello")
into()


# decorator allows to modify the behavious without changing the actual code