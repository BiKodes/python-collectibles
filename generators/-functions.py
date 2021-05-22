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

# Generating the first 10 perfect squares starting from 1:
def perfect_square():
    num = 1
    while(num <= 10):
        yield (num * num)
        num += 1
squares = perfect_square()
squares

next(squares)
next(squares)

# for-loop also accepts a generator:

for square in perfect_squares():
    print(square)

def cookies(value):
    while True:
        yield value

#Printing  a list of cookies

def print_cookies(cookies):
    length = len(cookies)
    for cookie in range(0, length):
        yield cookies[cookie]

cookie_list = ["Raspberry", "Choc-Chip", "Cinnamon", "Oat"]

for c in print_cookies(cookie_list):
	print(c)

# Totaling up a list of order prices:

order_list = [2.30, 2.50, 1.95, 6.00, 7.50, 2.15]

def total_orders(orders):
    length = len(orders)
    total = 0
    for o in range(0, length):
        total += orders[o]
        yield total

for order in total_orders(order_list):
    print(order)

# Reading Large Files:
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

# Generating an Infinite Sequence:

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i, end=" ")



