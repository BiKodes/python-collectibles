def multiplier(x):
    def inner_func(y):
        return x*y
    return inner_func

doubler = multiplier(2)

print(doubler(10))

tripler = multiplier(3)
print(tripler(10))

# a lambda can also be a closure:
multiplier = (lambda x: (lambda y: x*y))

doubler = multiplier(2)
print(doubler(10))

tripler = multiplier(3)
print(tripler(10))
