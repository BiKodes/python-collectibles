# Iterating Destructively With .popitem():

a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        print(f'{item} removed')

    except KeyError:
        print('The dictionary has no item now...')
        break

# map():
prices = {'Apple': 0.40, 'Orange': 0.35, 'Banana': 0.25}

def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))

new_prices = dict(map(discount, prices.items()))

print(new_prices)

# filter():
prices = {'Maembe': 0.40, 'Machungwa': 0.35, 'Papai': 0.25}

def has_low_price(price):
    return prices[price] < 0.4

low_price = list(filter(has_low_price, prices.keys()))
print(low_price)

# Using collections.ChainMap:
from collections import ChainMap

fruit_prices = {'Apple': 0.40, 'Orange': 0.35}
vegetable_prices = {'Pepper': 0.20, 'Onion': 0.55}
chained_dict = ChainMap(fruit_prices, vegetable_prices)

print(chained_dict) #ChainMap Object

for key in chained_dict:
    print(key, '-->', chained_dict[key])


for key, value in chained_dict.items():
    print(key, '--->', value)

# Using itertools:
# Cyclic Iteration With cycle():

from itertools import cycle

prices = {'Apple': 0.40, 'Orange': 0.35, 'Banana': 0.25}
times = 3  #Define how many times you need to iterate through prices
total_items = times * len(prices)

for item in cycle(prices.items()):
    if not total_items:
        break

    total_items -= 1
    print(item)

# Chained Iteration With chain():
from itertools import chain

fruit_prices = {'Apple': 0.40, 'Orange': 0.35, 'Banana': 0.25}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55, 'tomato': 0.42}

for item in chain(fruit_prices.items(), vegetable_prices.items()):
    print(item)

# Using the Dictionary Unpacking Operator (**):
fruit_prices = {'Apple': 0.40, 'Orange': 0.35}
vegetable_prices = {'Pilipili': 0.20, 'Vitunguu': 0.55}

unpacking_operator = {**vegetable_prices, **fruit_prices}

for k, v in {**vegetable_prices, **fruit_prices}.items():
    print(k, '--->', v)

# lambda functions:
# mainly used in combination with the functions filter(), map() and reduce().

# Initialize `fahrenheit` dictionary:
fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}

#Get the corresponding `celsius` values:
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary:
celsius_dict = dict(zip(fahrenheit.keys(),  celsius))

print(celsius_dict)

celsius = {k: (float(5)/9)*(v-32) for (k, v) in fahrenheit.items()}
print(celsius_dict)