# Classic Functional Constructs:
list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))

list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))

from functools import reduce
reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])

# Key Functions:
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids)) # Lexicographic sort

sorted_ids = sorted(ids, key=lambda x: int(x[2:]))
print(sorted_ids)

# UI Frameworks:
import _tkinter as tk
import  os

window = tk.Tk()
window.grid_columnconfigure(0, weight=1)
window.title("Lambda")
window.geometry("300*1000")
label = tk.Label(window, text="Lambda Calculus")
label.grid(column=0, row=0)
button = tk.Button(
    window,
    text="Reverse",
    command=lambda : label.configure(text=label.cget("text")[::-1]),
)

button.grid(column=0, row=1)
window.mainloop()

# Monkey Patching:
# asserting against predictable values in a repeatable manner
from contextlib import contextmanager
import secrets

def gen_token():
    """Generate a random token."""
    return f'TOKEN_{secrets.token_hex(8)}'

@contextmanager
def mock_token():
    """Context manager to monkey patch the secrets.token_hex function during testing."""
    default_token_hex = secrets.token_hex
    secrets.token_hex = lambda _:'feedfacecafebeef'
    yield
    secrets.token_hex = default_token_hex

def test_gen_key():
    """Test the random token."""
    with mock_token():
        assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"

test_gen_key()

# With pytest
def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'

def test_gen_key(monkeypatch):
    monkeypatch.setattr('secrets.token_hex', lambda _: 'feedfacecafebeef')
    assert gen_token() == f"TOKEN_{'feedfacecafebeef'}"


# Return Multiple Values:
# Return multiple values by packing them in a tuple:
findSquareCube = lambda num: (num**2, num**3)
x, y = findSquareCube(2)
print(x)
print(y)

# if else in a Lambda:
# you cannot use it in a lambda function.But you can use the if else ternary expression instead.

findMin = lambda x, y: x if x < y else y

print(findMin(2, 4))

print(findMin('a', 'x'))

# List Comprehension in a Lambda:
flatten = lambda l: [item for sublist in l for item in sublist]
L = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
print(flatten(L))

A = [['a', 'b', 'c'], ['d', 'e']]
print(flatten(A))

# Jump Table Using a Lambda:
# The jump table is a list or dictionary of functions to be called on demand.

# dictionary of functions:
exponent = {'square': lambda x: x**2,
            'cube': lambda x: x**3}

print(exponent['square'](3))

print(exponent['cube'](3))

# list of functions:
exponent = [lambda x: x**2,
            lambda x: x**3]

print(exponent[0](3))
print(exponent[1](3))


# Lambda Key Functions:

L = [('Sam', 35),
     ('Max', 25),
     ('Bob', 30)]

x = sorted(L, key=lambda student: student[1])
print(x)












