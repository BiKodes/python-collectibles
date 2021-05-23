new_generator = (x*x for x in range(5))
for each in new_generator:
    print(each)

def generatorGen():
    for x in range(5):
        yield x*x

newGen = generatorGen()

for each in newGen:
    print(each)

def multiYield():
    yield "Hello Biko"
    yield "Git It Great"
    yield "JavaScript Is Awesome"

for each in multiYield():
    print(each)

def multiYield():
    x = 5
    yield x
    x = x + 5
    yield x
    x = x * x
    yield x

for each in multiYield():
    print(each)

def printVal(l):
    for value in nums:
        yield value

nums = [10, 20, 30, 40, 50, 60]

g = printVal(nums)
print(next(g))

def fibo():
    first_num = 0
    second_num = 1
    yield second_num
    while(True):
        next_val = first_num + second_num
        yield next_val
        first_num, second_num = second_num, next_val

g = fibo()

# print(next(g))
# print(next(g))

for value in range(10):
    print(next(g))

for value in range(20):
    print(next(g))

#List comprehension

li = [10, 20, 30, 40, 50, 60]
qe = (value * value for value in li)
print(next(qe))

def new(dict):
    for x,y in dict.items():
        yield x,y

a = {1:"Hello", 2:"Biko Codes"}
b = new(a)
print(b)
next(b)
next(b)

def myfunc(i):
    while i <=3:
        yield i
        i += 1
j = myfunc(2)
next(j)

def ex():
    n = 3
    yield n
    n = n * n
    yield n

v = ex()
next(v)

f = range(6)
print("List Comp", end=":")
q = [x+2 for x in f]
print(q)
print("Gen Exp", end=":")
r = (x+2 for x in f)
print(r)

for x in r:
    print(x)

print(min(r))

#Fib

def fib():
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f + s

for x in fib():
    if x > 50:
        break
    print(x, end=" ")

#Number Stream

a = range(100)
b = (x for x in a)
print(b)

for y in b:
    print(y)

#Even Numbers Stream

a = range(2,100,2)
b = (x for x in a)
print(b)

for y in b:
    print(y)

#Odd Numbers Stream:
a = range(1,100,2)
b = (x for x in a)
print(b)

for y in b:
    print(y)