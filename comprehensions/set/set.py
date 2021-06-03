# Initialize a Set:
empty_set = set()

# intialize a set with values:
dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

# Add and Remove Values from Sets.
# Initialize set with values:
graphicDesigner = {'InDesign', 'Photoshop', 'Acrobat', 'Premiere', 'Bridge'}

# Add Values to a Set:
graphicDesigner.add('Illustrator')

# Remove Values from a Set:
graphicDesigner.remove('Illustrator')
graphicDesigner.discard('Premiere')
graphicDesigner.pop()

# Remove All Values from a Set:
graphicDesigner.clear()

# Iterate through a Set:
dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}

for skill in dataScientist:
    print(skill)

# Transform Set into Ordered Values:
type(sorted(dataScientist))
sorted(dataScientist, reverse=True)

# Remove Duplicates from a List:
print(list(set([1, 2, 3, 1, 7])))

# Use a list comprehension to remove duplicates from a list:
def remove_duplicates(original):
    unique = []
    [unique.append(n) for n in original if n not in unique]

    return(unique)

print(remove_duplicates([1, 2, 8, 3, 5, 1, 7, 8, 5]))

# The performance difference can be measured using the the timeit library which allows you to time your Python code.

import timeit

#Approach 1: Execution time
print(timeit.timeit('list(set([1, 2, 8, 3, 5, 1, 7, 8, 5]))', number=10000))

# Approach 2: Execution time
print(timeit.timeit('remove_duplicates([1, 2, 8, 3, 5, 1, 7, 8, 5])', globals=globals(), number=10000))

# Set Operation Methods:
dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])

dataEngineer = set(['Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'])

# union:
dataScientist.union(dataEngineer)
dataScientist | dataEngineer

# intersection:
dataScientist.intersection(dataEngineer)
dataScientist & dataEngineer

# You can test for disjoint sets by using the isdisjoint method:
graphicDesigner = {'Illustrator', 'InDesign', 'Photoshop'}

dataScientist.isdisjoint(dataEngineer)
dataScientist.isdisjoint(graphicDesigner)

# difference:
dataScientist.difference(dataEngineer)
dataScientist - dataEngineer

# symmetric_difference:
dataScientist.symmetric_difference(dataEngineer)

# Equivalent Result:
dataScientist ^ dataEngineer

