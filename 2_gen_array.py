import time


def csv_reader_not_generator(file_name):
    file = open(file_name)  # a generator is returned here
    result = file.read().split("\n")  # return a LIST of results
    file.close()
    return result


def create_new_array_no_generator(arr):
    new_arr = []
    for row in arr:
        row += "step_1"
        row += "step_2"
        row += "step_3"
        new_arr.append(row + "NEW LINE")
    return new_arr


def create_new_array_generator(arr):
    for row in arr:
        row += "step_1"
        row += "step_2"
        row += "step_3"
        yield (row + "NEW LINE")


# We want to iterate  this large list of rows in our file
arr = csv_reader_not_generator("big_file.txt")

# GOAL: Create a new array with with the values from previous array updated

print("\nNot using generator...")
start_time = time.time()
new_arr = create_new_array_no_generator(arr)
print("TOTAL_TIME:", time.time() - start_time)

print("Using generator...")
start_time = time.time()
new_arr = create_new_array_generator(arr)
print("TOTAL_TIME:", time.time() - start_time)

start_time = time.time()
new_arr = list(new_arr)
print("TOTAL_TIME AFTER ACCESSING :", time.time() - start_time)
