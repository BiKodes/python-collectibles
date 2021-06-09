lambda x: x + 1

(lambda x: x + 1)(2)

add_one = lambda x: x + 1
add_one(2)

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('Guido', 'Van Rossum')


(lambda x, y: x + y)(2, 3)

# A lambda function can be a higher-order function by taking a function (normal or lambda) as an argument like:

high_ord_func = lambda x, func: x + func(x)
high_ord_func(2, lambda x: x * 2)
high_ord_func(2, lambda x: x + 3)


# Functions:

import dis
add = lambda x, y: x + y
type(add)

dis.dis(add)

import dis
def add(x, y): return x + y
type(add)
dis.dis(add)

# Arguments.
# Positional arguments:
(lambda x, y, z: x + y + z)(1, 2, 3)
add = lambda x, y, z: x + y + z
print(add(2, 3, 4))

# Named arguments (sometimes called keyword arguments):
(lambda x, y, z=3: x + y + z)(1, 2)
(lambda x, y, z=3: x + y + z)(1, y=2)

add = lambda x, y, z: x + y + z
print(add(2, z=3, y=4))

# Default arguments:
add = lambda x, y=3, z=4: x + y + z
print(add(2))

# Variable list of arguments (often referred to as varargs):
(lambda *args: sum(args))(1, 2, 3)

add = lambda *args: sum(args)
print(add(2, 3, 4, 5))

# Variable list of keyword arguments:
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)

#Keyword-only arguments:
(lambda **kwargs: sum((kwargs.values())))(one=1, two=2, three=3)
add = lambda **kwargs: sum(kwargs.values())
print(add(x=2, y=3, z=4))

# Decorators:
def some_decorator(f):
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")

# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
    return wrap

# Applying decorator to a function:
@trace
def add_two(x):
    return x + 2

# Calling the decorated function:
add_two(3)

# Applying decorator to a lambda:
print((trace(lambda x: x ** 2))(3))

list(map(trace(lambda x: x*2), range(3)))

# Closure
# closure constructed with a normal Python function:
def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y +z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

# a lambda can also be a closure:
def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

# Evaluation Time:

def wrap(n):
    def f():
        print(n)
    return f

numbers = 'One', 'Two', 'Three'
funcs = []

for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()

def wrap(n):
    def f():
        print(n)
    return f

numbers = 'moja', 'mbili', 'tatu'
funcs = []

for n in numbers:
    funcs.append(lambda n=n: print(n))

for f in funcs:
    f()

# Single Expression Only:
evenOdd = (lambda x:
           'odd' if x%2 else 'even')

# Immediately Invoked Function Expression:
print((lambda x: x*2)(3))

# Multiple Arguments:
mul = lambda x, y: x*y
print(mul(2, 3))

add = lambda x, y, z: x + y + z
print(add(2, 5, 10))



















