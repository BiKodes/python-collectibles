iter('foobar')
iter(['foo', 'bar', 'baz'])
iter(('foo', 'bar', 'baz'))
iter({'foo', 'bar', 'baz'})
iter({'foo': 1, 'bar': 2, 'baz': 3})


# Iterating Through a Dictionary:
d = {'foo': 1, 'bar': 2, 'baz': 3}

# getting keys:
for k in d:
    print(k)

# getting values:
for k in d:
    print(d[k])

for v in d.values():
    print(v)

i, j = (1, 2)

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

d = {'foo': 1, 'bar': 2, 'baz': 3}
d.items()

d = {'foo': 1, 'bar': 2, 'baz': 3}

for k, v in d.items():
    print('k =', k, ', v=', v)













