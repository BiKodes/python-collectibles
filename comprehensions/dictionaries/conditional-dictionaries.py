# IF Statements:

ages = {
    'kevin': 12,
    'marcus': 9,
    'evan': 28,
    'Biko': 30
}

new_ages = {key:value for (key, value) in ages.items() if value > 25}
print(new_ages)

# Adding Multiple IF Statements:

ages = {
    'bob': 58,
    'lee': 20,
    'ibra': 23,
    'dave': 19,
    'moh': 28,
    'jane': 24,
    'oti': 33
}

younger = {key: value for (key, value) in ages.items() if value < 25 if value % 2 == 0}
print(younger)

# If Else:

ages = {
    'Yusuf': 32,
    'Sikujua': 25,
    'Machio': 30,
    'Ojasi': 28,
    'Alvo': 21,
    'Nuri': 33
}

oddeven = {key: ('odd' if value % 2 == 1 else 'even') for (key, value) in ages.items()}
print(oddeven)

# Nested Dictionary Comprehension:

mutiples = {
    key1: {
        key2: key1 * key2
        for key2 in range(1, 6)
    }
    for key1 in range(10, 60, 10)
}

print(mutiples)

# Filtering Items:
a_dict = {'Moja': 1, 'Mbili': 2, 'Tatu': 3, 'Nne': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}
print(new_dict)

# Conditionals to Dictionary Comprehension:
# If Condition:
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Check for items greater than 2:
dict1_cond = {k:v for (k, v) in dict1.items() if v>2}
print(dict1_cond)

# Multiple If Conditions:
# items greater than 2 & they are multiples of 2 at the same time.

dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
print(dict1_doubleCond)

dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

dict2_tripleCond = {k:v for (k, v) in dict2.items() if v>2 if v%2 == 0 if v%3 == 0}
print(dict2_tripleCond)

# If-Else Conditions:
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

# Identify odd and even entries:
dict1_tripleCond = {k: ('even' if v%2 == 0 else 'odd') for (k,v) in dict1.items()}

print(dict1_tripleCond)

# Nested Dictionary Comprehension:
nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()}
              for (outer_k, outer_v) in nested_dict.items()}

print(float_dict)














