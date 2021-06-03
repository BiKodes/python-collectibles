# Inner Functions:
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

# Returning Functions From Functions:

def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child

    else:
        return second_child

first = parent(1)
second = parent(2)

# Simple Decorators:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

say_whee()

# Only run the decorated code during the day:

from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass #Hash, the neighbours are a sleep

    return  wrapper

def say_whee():
    print("Wheee!")

say_whee = not_during_the_night(say_whee)


# Syntactic Sugar!
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Wheee!")

# Reusing Decorators:
from decorators import do_twice

@do_twice
def say_whee():
    print("Wheee!")

# Decorating Functions With Arguments:
from decorators import  do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

# Returning Values From Decorated Functions:
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam")

print(hi_adam)

return_greeting("Biko")
