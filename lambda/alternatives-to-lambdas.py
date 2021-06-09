# Map:
list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))

# Using a list comprehension eliminates the need for defining and invoking the lambda function:

[x.capitalize() for x in ['cat', 'dog', 'cow']]

# a map() function without a lambda:
def doubler(x):
    return x*2

L = [1, 2, 3, 4, 5, 6]
mod_list = map(doubler, L)
print(list(mod_list))

# Double each item of the list:
L = [1, 2, 3, 4, 5, 6]
doubler = map(lambda x: x*2, L)
print(list(doubler))


# Filter:
even = lambda x: x%2 == 0
list(filter(even, range(11)))

# mentation leveraging the list comprehension construct give
[x for x in range(11) if x%2 == 0]

# without a lambda:
def checkAge(age):
    if age > 18:
        return True
    else:
        return False

age = [5, 11, 16, 19, 24, 42]
adults = filter(checkAge, age)
print(list(adults))

# replaced by a lambda:
age = [5, 11, 16, 19, 24, 42]
adults = filter(lambda x: x > 18, age)
print(list(adults))

# Reduce:
# It applies a rolling calculation to all items in a list. You can use it to calculate the total sum or
# to multiply all the numbers together.
# apply reduce() to a list of pairs and calculate the sum of the first item of each pair
import functools
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)

#  using a generator expression
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
sum(x[0] for x in pairs)

#  underscore (_) is a Python convention indicating that you can ignore the second value of the pair.
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
sum(x for x, _ in pairs)

# reduce() function without a lambda:
from functools import reduce

def summer(a, b):
    return  a + b

L = [10, 20, 30, 40]
result = reduce(summer, L)
print(result)

# with reduce() function:
L = [10, 20, 30, 40]
result = reduce(lambda a, b: a + b, L)
print(result)









