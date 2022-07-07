import itertools
import sys
from typing import Iterable


def square_list_with_gen(arr: Iterable):
    return (x * x for x in arr)


def cube_list_with_gen(arr: Iterable):
    return (x * x * x for x in arr)


def divide_list_with_gen(arr: Iterable):
    return (x // 2 for x in arr)


X = range(1000)

# We want to use an intermediary processing step for two different arrays
X_processed = square_list_with_gen(X)
print(type(X_processed))
X_version_1 = cube_list_with_gen(X_processed)
X_version_2 = divide_list_with_gen(X_processed)
print(list(X_version_1))
print(list(X_version_2)) # nothing will be here 

# one approach to solving this problem
X_processed = square_list_with_gen(X)
print(type(X_processed))
X_version_1 = cube_list_with_gen(X_processed)
X_processed = square_list_with_gen(X)
X_version_2 = divide_list_with_gen(X_processed)
print(list(X_version_1))
print(list(X_version_2))



# Using itertools.tee library to solve this appraoch
X_processed = square_list_with_gen(X)

# create copies of our generator objects
X_copy_1, X_copy_2, dummy = itertools.tee(X_processed, 3)

# the copies don't take much space
print(f"{sys.getsizeof(X_processed)}")
print(f"{sys.getsizeof(X_copy_1)}, {sys.getsizeof(X_copy_2)}, {sys.getsizeof(dummy)}")

X_version_1
X_version_1 = list(cube_list_with_gen(X_copy_1)) # evaluate the generator object
X_version_2 = list(divide_list_with_gen(X_copy_2)) # evaluate the generator object

print("X_version_1 memory:", sys.getsizeof(X_version_1))
print("X_version_2 memory:", sys.getsizeof(X_version_2))


# print(list(dummy)[1:3])
