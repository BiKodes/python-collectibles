# Map:
list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))

# Using a list comprehension eliminates the need for defining and invoking the lambda function:

[x.capitalize() for x in ['cat', 'dog', 'cow']]

# Filter:
even = lambda x: x%2 == 0
list(filter(even, range(11)))

# mentation leveraging the list comprehension construct give
[x for x in range(11) if x%2 == 0]

# Reduce:
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