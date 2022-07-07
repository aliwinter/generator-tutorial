# Generator Tutorials
This repository will go over the main ways we intend to use generators when working with different types of lists or iterables in python.

## __Purpose__
The purpose of using generators is that they help us deal with one object in memory at a time, when we want to perform operations which require a list of objects to be used we will often try to use a generator to reduce the memory consumption.  Since Generators don't hold in memeory the whole array they just operate on the individual elements of an iterable themselves.


## __Start__
Go through the different files and see how arrays can be adopted to be turned into generator arrayts and how functions can be turned into generator functions.


### __Generators with List Comprehensions__

You can easily convert python list comprehensions to generator comprehensions by one simple technique.

__List Comprehension__
```python
def square_list_no_gen(arr: Iterable):
    return [x * x for x in arr]
```

__Generator Comprehension__
```python
def square_list_with_gen(arr: Iterable):
    return (x * x for x in arr)
```

A regular list comprehension uses Square brackets and a generator comprehension uses round brackets to enclose the short form syntax.  Look at `1_gen_list_comprehension.py` for an example on the time and memory tradeoffs.


### __Generators with lists__


__Functions with List__
When we apply some processing on arrays we sometimes use temporary arrays to store the intermediate values of the array like the following

```python
arr = [1,2,3,4,5]
def square_numbers(arr):
    arr_squared = []
    for x in arr:
        arr_squared.append(x*x)
    return arr_squared
arr = square_numbers(arr)
print(arr) # [1,4,9,16,25]
```

__Generator Functions__
This is how you would apply the same Function which uses temporary arrays 
```python
arr = [1,2,3,4,5]
def square_numbers(arr):
    for x in arr:
        yeild (x*x)
arr = square_numbers(arr)
print(arr) # [1,4,9,16,25]
```

look at the `2_gen_array.py` script for an example of the time and memory tradeoffs.


### Using Multiple Generators
The thing about generators is that once you iterate through one generator you can't iterate through it again, another way to say this is that generators are one time use lists which can't be iterated on again.  To get around this we create duplicates of iterators, which we can use multiple times to help use with processing jobs.


__Duplicating Generators__
```python
import itertools
arr = [1,2,3,4,5] # list

arr = (x * x for x in arr) # gen

arr_copy_1, arr_copy_2 = itertools.tee(arr, 2) # two generators from this one

new_arr_1 = (x * x for x in arr_copy_1) 

new_arr_2 = (x // x for x in arr_copy_2)
```

look at the `3_gen_itertools.py` script for an example of the time and memory tradeoffs.


