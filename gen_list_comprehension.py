import time
from typing import Iterable


def square_list_no_gen(arr: Iterable):
    """Uses List Comprehension Short form to update an array"""
    return [x * x for x in arr]


def square_list_with_gen(arr: Iterable):
    return (x * x for x in arr)


def cube_list_with_gen(arr: Iterable):
    return (x * x * x for x in arr)


arr = range(10000)

start = time.time()
new_arr = square_list_no_gen(arr)
print(f"Total time without generator: {time.time()-start}\n")

start = time.time()
temp_arr = square_list_with_gen(arr)
new_arr = cube_list_with_gen(temp_arr)

print(f"Total time with generator: {time.time()-start}")

# when we access the array at the end then it actually performs
# all the computation
start = time.time()
arr = list(new_arr)
print(f"Total time after generator accessed: {time.time()-start}")
