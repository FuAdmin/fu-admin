from django.test import TestCase

# Create your tests here.
def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

@debug
def hello():
    print("hello")

hello()