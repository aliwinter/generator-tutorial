import itertools
from typing import Iterable


def square_list_with_gen(arr: Iterable):
    return (x * x for x in arr)


def cube_list_with_gen(arr: Iterable):
    return (x * x * x for x in arr)


def divide_list_with_gen(arr: Iterable):
    return (x // 2 for x in arr)


X = range(10)

# We want to use an intermediary processing step for two different arrays
X_processed = square_list_with_gen(X)
X_version_1 = cube_list_with_gen(X_processed)
X_version_2 = divide_list_with_gen(X_processed)
print(list(X_version_1))
print(list(X_version_2))

X_processed = square_list_with_gen(X)
X_copy_1, X_copy_2 = itertools.tee(X_processed)

X_version_1 = cube_list_with_gen(X_copy_1)
X_version_2 = divide_list_with_gen(X_copy_2)
print(list(X_version_1))
print(list(X_version_2))
