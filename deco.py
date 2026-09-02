def decorator(func):
    def wrapper():
        print("This is header from decorator")
        func()
        print("This is footer from decorator")
    return wrapper
@decorator
def  test():
    print("Hello Test")

test()