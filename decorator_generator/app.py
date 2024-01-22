def my_decorator(fn):
    def wrapper():
        print("before function runs")
        fn()
        print("after function runs")
    return wrapper


@my_decorator
def greet():
    print("hello my friend")


greet()


def countdown(n):
    while n > 0:
        yield n
        n -= 1


for i in countdown(5):
    print(i)
