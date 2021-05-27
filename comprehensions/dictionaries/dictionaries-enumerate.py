# Using the Enumerate Function:
names = {'Biko', 'Amir', 'Steven', 'Hekima'}
index = {k: v for (k, v) in enumerate(names)}
print(index)

index = {k: v for (v, k) in enumerate(names)}

# Extracting a Subset of a Dictionary:
bigdict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
smalldict = {k: bigdict[k] for k in ('a', 'b', 'c')}
print(smalldict)

# Remove Items for a Dictionary:
ages = {
    'kevin': 12,
    'marcus': 9,
    'evan': 31,
    'nik': 31
}

ages = {key: ages[key] for key in ages.keys() - {'marcus', 'nik'}}
print(ages)

# Reverse Key:Value in Dictionary:

dictionary = {'key1': 'value1', 'key2':'value2'}
dictionary_new = {value: key for (key: value) in dictionary}

user = {
    'name': 'nik',
    'age': 31,
    'company': 'datagy'
}

user_reversed = {v: k for (k, v) in user.items()}
print(user_reversed)