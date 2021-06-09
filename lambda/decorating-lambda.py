from functools import wraps

# Defining a decorator:

def debug(func):
    @wraps
    def wrapper(*args, **kwargs):
        result = func(*args)
        print(f"[DEBUG] Calling {func.__name__} with argument {args} | Result: {result}")
        return result
    return wrapper


# Applying decorator to hello():
@debug
def hello(name):
    return "Hello " + name

# Calling the decorated function:
print(hello("Biko"))

# Apply our @debug decorator to a lambda

print((debug(lambda x: x**2))(3))

print(list(map(debug(lambda x: x*2), range(3))))