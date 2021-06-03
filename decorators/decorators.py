# Nested Function:

def outer_function():
    def inner_function():
        print("Inside the inner function")

    return inner_function

inner_function = outer_function()
print(type(inner_function))
inner_function()

# Pass function as an argument:
def inner_function():
    print("Inside the inner function")

def outer_function(func):
    func()

outer_function(inner_function)

# Decorators:

def function_to_be_called():
    print("This is the main function")

def decorator_function(func):
    def inner():
        print("Before execution of the function")
        func()
        print("After execution of the function")

    return inner

function_to_be_called = decorator_function(function_to_be_called)
function_to_be_called()

def decorator_function(func):
    def inner():
        print("Before execution of the function")
        func()
        print("After execution of the function")
    return inner

@decorator_function
def function_to_be_called():
    print("This is the main function")

function_to_be_called()


# What is functools.wraps():

def decorator_function(func):
    def inner():
        '''
            This function extends the function be called
        '''
        print("Before execution of the function")
        func()
        print("After execution of the function")
    return inner

@decorator_function
def first_function():
    print("This is the first function")

@decorator_function
def second_function():
    print("This is the second function")

print(first_function.__name__)
print(first_function.__doc__)
print(second_function.__name__)
print(second_function.__doc__)

# One workaround will be manually assigning the name and docstring:
def decorator_function(func):
    def inner():
        '''
            This function extends the function be called
        '''
        print("Before execution of the function")
        func()
        print("After execution of the function")

    # manually assigning name and docstrings
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__

    return inner

@decorator_function
def first_function():
    '''
      Docstring for 1st function
    '''
    print("This is the first function")

@decorator_function
def second_function():
    '''
       Docstring for 2nd function
    '''
    print("This is the second function")

print(first_function.__name__)
print(first_function.__doc__)
print(second_function.__name__)
print(second_function.__doc__)

# use functools.wraps as a decorator to the inner function, to save time as well as to increase readability:

from functools import wraps

def decorator_function(func):
    @wraps(func)
    def inner():
        '''
          This function extends the function be called
        '''

        print("Before execution of the function")
        func()
        print("After execution of the function")
    return inner

@decorator_function
def first_function():
    '''
        Docstring for 1st function
    '''
    print("This is the first function")

@decorator_function
def second_function():
    '''
       Docstring for 2nd function
    '''
    print("This is the second function")

print(first_function.__name__)
print(first_function.__doc__)
print(second_function.__name__)
print(second_function.__doc__)


# Multiple Decorators:
def uppercase_convertor(func):
    @wraps(func)
    def wrapper():
        var = func()
        return var.upper()

    return wrapper

def split_string(func):
    @wraps(func)
    def wrapper():
        var = func()
        return var.split()
    return wrapper

@split_string
@uppercase_convertor
def sample_function():
    return 'Hello World'

output = sample_function()
print(output)




