# using if statement:
num = [i for i in range(10) if i % 2 == 0]
print(num)

# using if without else:
num = [i for i in range(10) if i>=5]
print(num)

#Using nested if statement:
num = [i for i in range(50) if i%2==0 if i%3==0 if i%3==0]
print(num)

# using multiple if statement:

num = [i for i in range(30) if i>=2 if i<=25 if i%4==0 if i%8==0]
print(num)

# with if-else:
fruits = ["mango" if i%3==0 else "orange" for i in range(10)]
print(fruits)

# using nested for loop:
for i in range(2,4):
    for j in range(1,5):
        print(f"{i}+{j}={i+j}")

# transposes rows and columns:

list = [[2, 4, 6, 8]]
matrix = [[row[i] for row in list] for i in range(4)]
print(matrix)

#List

words = [
    "Serendipity",
    "Petrichor",
    "Supine",
    "Solitude",
    "Aurora",
    "Idyllic",
    "Clinomania",
    "Pluviophile",
    "Euphoria",
    "Sequoia"]

# Single loop/if statement:
# derive a new list which only keeps the elements with length less than 8 from the original list:
short_words = [word for word in words if len(word) < 8]
print(short_words)

# Multiple if statements:
short_words = [word for word in words if len(word) < 8 if word.startswith("S")]
print(short_words)

# use or in the if statement:
short_or_s_words = [word for word in words if len(words) < 8 or word.startswith("S")]
print(short_or_s_words)

# Multiple loop/if statement:
# transform a nested list into a flatten list, you can make use of the list comprehension with multiple loops:

lat_long = [[1.291173, 103.810535], [1.285387, 103.846082], [1.285803, 103.845392]]

flat_long = [x for pos in lat_long for x in pos]
print(flat_long)

# multiple sequences to be iterated through, you can have multiple for statements in your comprehension or
# use zip function

new_words = [(word, num) for word in words if word.startswith("S") for num in range(4) if num%2==0]
print(new_words)

# use zip:
zip_words = [(word, num) for word, num in zip(words, range(len(words))) if word.startswith("S") and num%2 == 0]

# return the particular type of files from the current and its sub folders:
import os

files_return = [os.path.join(d[0], f) for d in os.walk(".") if not ".ipynb_checkpoints" in d[0]
                for f in d[2] if f.endswith(".ipynb")]
print(files_return)

# Generate tuples from list comprehension:
tuples_list = [(word, len(word)) for word in words]
print(tuples_list)

# Iterating through a string Using for Loop:

h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

# Iterating through a string Using List Comprehension:
h_letters = [letter for letter in 'human']
print(h_letters)

# List Comprehensions vs Lambda functions:
# Using Lambda functions inside List
letters = list(map(lambda x: x, 'human'))
print(letters)

# Conditionals in List Comprehension:
# Using if

number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

# Nested IF:
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

# if...else :
obj = ["Even" if i%2 == 0 else "Odd" for i in range(10)]
print(obj)

# Nested Loops:
# Transpose of Matrix using Nested Loops
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)

print(transposed)

#Transpose of a Matrix using List Comprehension:
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)