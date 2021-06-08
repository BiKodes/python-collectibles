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
