def decorator(func):
    def wrapper():
        print("Before fn")
        func()
        print("Code after fn")
    return wrapper

@decorator
def show():
    print("I am usual function")
    
show()
#dec = decorator(show)
#dec()