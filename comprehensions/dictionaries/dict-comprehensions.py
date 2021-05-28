# Creating Squares of Numbers:
squares = {i:i**2 for i in [1, 2, 3, 4, 5]}
print(squares)

# Changing from Kilograms to Pounds:

old_weights = {
    'book': 0.5,
    'milk': 2.0,
    'tv': 7.0
}

new_weights = {key: value*2.2 for (key, value) in old_weights.items()}
print(new_weights)

# to create  new dictionary from lists:
objects = ['Blue', 'Zabibu', 'Sokwe']
categories = ['Color', 'Matunda', 'Pet']

a_dict = {key: value for key, value in zip(categories, objects)}
print(a_dict)

# Turning Keys Into Values and Vice Versa:
a_dict = {'moja': 1, 'mbili': 2, 'tatu': 3, 'nne': 4}
new_dict = {value: key for key, value in a_dict.items()}
new_dict

# Doing Some Calculations:
incomes = {'maembe': 5600.00, 'zambarau': 3500.00, 'tofa': 5000.00}
total_income = sum([value for value in incomes.values()])
print(total_income)

total_income = sum(value for value in incomes.values())
print(total_income)

total_income = sum(incomes.values())
print(total_income)

# Removing Specific Items:
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
non_citric = {k: incomes[k] for k in incomes.keys() - {'orange'}}
print(non_citric)

# Sorting a Dictionary:
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_income = {k: incomes[k] for k in sorted(incomes)}
print(sorted_income)

# Iterating in Sorted Order:
# Sorted by Keys:
incomes = {'Apple': 5600.00, 'Orange': 3500.00, 'Banana': 5000.00}
for key in sorted(incomes):
    print(key, '--->', incomes[key])

# Sorted by Values:

incomes = {'Apple': 5600.00, 'Orange': 3500.00, 'Banana': 5000.00}

def by_value(item):
    return item[1]

for k, v in sorted(incomes.items(), key=by_value):
    print(k, '--->', v)


# iterating through the values of a dictionary in sorted order, without worrying about the keys:

for value in sorted(incomes.values()):
    print(value)

# Reversed:
incomes = {'Apple': 5600.00, 'Orange': 3500.00, 'Banana': 5000.00}

for key in sorted(incomes, reverse=True):
    print(key, '--->', incomes[key])

# initialize a dictionary:
a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
a['doughnut'] = 'snack'
print(a['apple'])

a = {'one': 1, 'two': 'to', 'three': 3.0, 'four': [4,4.0]}
print(a)


# Update a dictionary
a['one'] = 1.0
print(a)

# Delete a single element:
del a['one']
print(a)

# Delete all elements in the dictionary:
a.clear()
print(a)

# Delete the dictionary:
del a
print(a)

# Delete a single element:
del a['one']
print(a)

# Delete all elements in the dictionary:
a.clear()
print(a)


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

double_dict1 = {k: v*2 for (k, v) in dict1.items()}
print(double_dict1)

# change the names of the key:
dict1_keys = {k*2: v for (k, v) in dict1.items()}
print(dict1_keys)

numbers = range(10)
new_dict_for = {}

#Add values to 'new_dict' using for loop:

for n in numbers:
    if n % 2 == 0:
        new_dict_for[n] = n**2

print(new_dict_for)

# Use dictionary comprehension:
new_dict_comp = {n: n*2 for n in numbers if n%2 == 0}

print(new_dict_comp)