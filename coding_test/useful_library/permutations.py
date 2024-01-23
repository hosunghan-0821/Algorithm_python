from itertools import *

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result)
print(len(result))
result = list(permutations(data, 3))
print(result)
print(len(result))
