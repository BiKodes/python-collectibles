{skill for skill in ['SQL', 'SQL', 'PYTHON', 'PYTHON']}

{skill for skill in ['GIT', 'PYTHON', 'SQL']if skill not in {'GIT', 'PYTHON', 'JAVA'}}

# Membership Tests:
possibleList = ['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS', 'Java', 'Spark', 'Scala']
'Python' in possibleList

possibleSet = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS', 'Java', 'Spark', 'Scala'}
'Python' in possibleSet

# Subset:
possibleSkills = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
mySkills = {'Python', 'R'}

mySkills.issubset(possibleSkills)

# Frozensets:
# Nested lists and tuples:
nestedLists = [['the', 12], ['to', 11], ['of', 9], ['and', 7], ['that', 6]]
nestedTuples = (('the', 12), ('to', 11), ('of', 9), ('and', 7), ('that', 6))

nestedSets = set([frozenset()])












