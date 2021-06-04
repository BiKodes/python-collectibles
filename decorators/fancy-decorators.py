# Decorating Classes:
# The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are
# not connected to a particular instance of that class. The @property decorator is used to customize getters
# and setters for class attributes.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535

from decoratorexamples import debug, timer

class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

# Nesting Decorators:
from decoratorexamples import debug
from decorators import   do_twice

@debug
@do_twice
def greet(name):
    print(f"Hello {name}")

greet("Baraka")

@do_twice
@debug
def greet(name):
    print(f"Hello {name}")

greet("Furaha")

# Decorators With Arguments:
import functools
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")


# The decorators that can be used both with and without arguments.
import functools
def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


@repeat
def say_whee():
    print('Wheee!')

@repeat(num_times=3)
def greet(name):
    print(f"Jambo {name}")






















