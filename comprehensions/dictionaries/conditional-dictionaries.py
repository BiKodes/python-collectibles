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
