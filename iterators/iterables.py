a = ['foo', 'bar', 'baz']
itr = iter(a)
itr
next(itr)
next(itr)
next(itr)

# You can define two independent iterators on the same iterable object:
a = ['foo', 'bar', 'baz']
itr1 = itr(a)
itr2 = itr(a)

next(itr1)
next(itr2)

# grab all the values from an iterator:
a = ['foo', 'bar', 'baz']
itr = iter(a)
list(itr)
tuple(itr)
set(itr)

# Altering for Loop Behavior.
# break and continue Statements:
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

# else Clause:
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')

for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)

else:
    print('Done')

# Iterating Through an Iterator:

my_list = [4, 7, 0, 3]

#get an iterator using iter()
my_iter = iter(my_list)

#  iterate through it using next()
next(my_iter)

# Working of for loop for Iterators:
# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

# Building Custom Iterators:
class PowTwo:
    """Class to implement an iterator of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.max = max

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result

        else:
            raise StopIteration

#create an object
numbers = PowTwo(3)

#create an iterable from the object
i = iter(numbers)

#Using next to get to the next iterator element
print(next(i))
print(next(i))

# Python Infinite Iterators:
class InfIter:
    """Infinite iterator to return all odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num









