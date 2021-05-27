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

