# use a context manager to process the data.txt file:
with open('data.txt') as f:
    data = f.readlines()
    print(int(data[0]))

# how to access the f variable after the with statement:
with open('data.txt') as f:
    data = f.readlines()
    print(int(data[0]))

print(f.closed)

# simple implementation of the open() function using the context manager protocol:
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print(f'Opening the file {self.filename}.')
        self.__file = open(self.filename, self.mode)
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Closing the file {self.filename}.')

        if not self.__file.closed:
            self.__file.close()

        return False

with File('data.txt', 'r') as f:
    print(int(next(f)))

# Using Python context manager to implement the start and stop pattern:
# This defines a Timer class that supports the context manager protocol

from time import perf_counter

class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False

# use the Timer class to measure the time needed to calculate the Fibonacci of 1000, one million times:

def fibonacci(n):
    f1 = 1
    f2 = 1

    for i in range(n-1):
        f1, f2 = f2, f1 + f2

    return f1

with Timer() as timer:
    for _ in range(1, 1000000):
        fibonacci(1000)

print(timer.elapsed)
























