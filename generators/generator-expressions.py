# List comprehension produces the complete list of items at once:
a = range(6)
print("List comprehension", end=':')
b = [x + 2 for x in a]
print(b)

# generator expression which returns the same items but one at a time:
print("Generator expression", end=':n')
c=(x+2 for x in a)
print(c)
for y in c:
    print(y)

# Generator functions can be used within other functions as well:
a = range(6)
print("Generator expression", end=':n')
c = (x+2 for x in a)
print(c)
print(min(c))