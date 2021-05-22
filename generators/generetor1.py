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

