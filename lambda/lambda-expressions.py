# Raising an Exception:
def throw(ex):
    raise ex

(lambda : throw(Exception('Something bad happened')))()

# Cryptic Style:
(lambda _: list(map(lambda _: _ // 2, _)))([1,2,3,4,5,6,7,8,9,10])

# upgrade to this lambda code could be to name the variables:
(lambda some_list: list(map(lambda n: n//2,
                            some_list)))([1,2,3,4,5,6,7,8,9,10])

# Python Classes:
# You can but should not write class methods as Python lambda functions.

class Car:
    """Car with methods as lambda functions."""
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    brand = property(lambda self: getattr(self, '_brand'),
                     lambda self, value: setattr(self, '_brand', value))

    year = property(lambda self: getattr(self, '_year'),
                    lambda self, value: setattr(self, '_year', value))

    __str__ = lambda self: f'{self.brand} {self.year}'

    honk = lambda self: print('Honk!')

# Proper implementation of __str__ should be as follows:
def __str__(self):
    return f'{self.brand} {self.year}'

#brand shoul be as follows:

@property
def brand(self):
    return self._brand

@brand.setter
def brand(self, value):
    self._brand = value

