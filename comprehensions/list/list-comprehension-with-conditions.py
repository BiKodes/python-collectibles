feet = [40, 36.5, 37.5, 36]
uneven = [x/2 for x in feet if x%2 == 0]
print(uneven)

# with a Python for loop:
# Initialize and empty list `uneven`:
uneven = []

#Add values to even:
for x in feet:
    if x % 2 == 0:
        x = x / 2
        uneven.append(x)

print(uneven)

# Multiple If Conditions:

divided = []

for x in range(100):
    if x%2 == 0:
        if x%6 == 0:
            divided.append(x)

print(divided)

divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]
print(divided)


# If-Else Conditions:
[x + 1 if x >= 120000 else x+5 for x in feet]

#For Loop:

for x in feet:
    if x >= 120000:
        x + 1

    else:
        x+5

print(feet)

# Nested List Comprehensions:

list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8]]

# Flatten `list_of_list`:
flatten = [y for x in list_of_list for y in x]


matrix = [[1, 2, 3 ], [4, 5, 6], [7, 8, 9]]

new_matrix = [[row[i] for row in matrix] for i in range(3)]

transposed = []

for i in range(3):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])

    transposed.append(transposed_row)

# nested list comprehensions when you need to create a list of lists that is a matrix:
matrix = [[0 for col in range(4) for row in range(3)]]

matrix

int_matrix = [[int(x) for x in feet] for x in feet]