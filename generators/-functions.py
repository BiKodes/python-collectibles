# a generator that yields items instead of returning a list:

def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))

def func(a):
    yield  a

a = [1, 2, 3]
b = func(a)
next(b)

a = 0
def myfunc(a):
    while a >= 3:
        yield a
        a = a + 1

b = myfunc(a)

print(b)
next(b)

a = 2
def myfunc(a):
    while a >= 0:
        yield a
        a -= 1

b = myfunc(a)

print(b)
next(b)

# Generators with loops:

def z():
    n = 1
    yield n
    n = n +3
    yield n

for x in z():
    print(x)

# Generating Fibonacci Series:
def fibo():
    first, second = 0,1
    while True:
        yield first
        first, second = second, first+second

for x in fibo():
    if x > 50:
        break
    print(x, end=" ")
