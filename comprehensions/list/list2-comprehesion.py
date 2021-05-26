S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]


#With For Loops:
number = range(10)

#Initialize 'new_list':
new_list = []

#Add values to 'new_list':
for n in numbers:
    if n%2==0:
        new_list.append(n**2)

print(new_list)

#Same with list comprehension:

new_list = [n**2 for n in numbers if n%2 == 0]
print(new_list)