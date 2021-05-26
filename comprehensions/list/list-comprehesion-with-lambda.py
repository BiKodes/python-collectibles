# Replace map() in Combination with Lambda Functions:
#Initialize the `kilometer` list
kilometer = [39.2, 36.5, 37.5, 37.9]

# Construct `feet` with `map()`
feet = map(lambda x: float(3280.8399)*x, kilometer)

#Print 'feet' as a list:
print(list(feet))

# Convert `kilometer` to `feet`:
feet = [float(3280.8399)*x for x in kilometer]

#Print `feet`:
print(feet)

# filter() and Lambda Functions to List Comprehensions:
# Map the values of `feet` to integers:
feet = list(map(int, feet))

# Filter `feet` to only include uneven distances:
uneven = filter(lambda x: x%2, feet)

# Check the type of `uneven`:
type(uneven)

# Print `uneven` as a list:
print(list(uneven))

# Constructing `feet`:
feet = [int(x) for x in feet]

#Print `feet`:
print(feet)

# Get all uneven distances:


#Print `Uneven`:
print(uneven)

# reduce() and Lambda Functions in Python:
# Import `reduce` from `functools`:
from functools import  reduce

# Reduce `feet` to `reduced_feet`:
reduced_feet = reduce(lambda x,y: x+y, feet)

print(reduced_feet)

# Construct `reduced_feet`:
reduced_feet = sum([x for x in feet])

print(reduced_feet)

