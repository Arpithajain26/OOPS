def decorator(fuc):
    def wrapper(a,b):
        print("result ",end="")
        fuc(a,b)
    return wrapper
@decorator
def add(a,b):
    print(a+b)
add(2,3)