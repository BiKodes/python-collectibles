simpsons = "Homer Simpson is son of Abraham Simpson and Father of Bart Simpson"
chars = simpsons.split()
simpsons_set = {word for word in chars}
print(simpsons_set)

# Adding conditions ~ comparison operator:
simpsons_set = {word for word in chars if len(word) >= 4}
print(simpsons_set)

# Nested Set:
simpsons1 = "Homer Simpson is son of Abraham Simpson and Father of Bart Simpson"
chars = simpsons1.split()
vowels = ['a', 'e', 'i', 'o', 'u']
constants = {frozenset(
    {letter for letter in word if letter not in vowels}) for word in chars}
print(constants)

# convert the tags in the set to another set of tags in lowercase:
tags = {'Django', 'Pandas', 'Numpy'}

lowercase_tags = set()

for tag in tags:
    lowercase_tags.add(tag.lower())

print(lowercase_tags)

# using map() function with a lambda expression:
tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = set(map(lambda tag: tag.lower(), tags))

print(lowercase_tags)

tags = {'Django', 'Pandas', 'Numpy'}
lowercase_tags = {tag.lower() for tag in tags}
print(lowercase_tags)

# Converting all elements of the tags set to lowercase except for the Numpy:
tags = {'Django', 'Pandas', 'Numpy'}
new_tags = {tag.lower() for tag in tags if tag != 'Numpy'}
print(new_tags)