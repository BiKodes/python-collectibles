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

