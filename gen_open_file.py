import time


def csv_reader_not_generator(file_name):
    file = open(file_name)  # a generator is returned here
    result = file.read().split("\n")  # return a LIST of results
    file.close()
    return result


def csv_reader_generator(file_name):
    # open(file_name, "r") -> returns a generator
    f = open(file_name, "r")
    for row in f:
        yield row  # returns a generator object
    f.close()


print("Using generator...")
start_time = time.time()
csv_gen = csv_reader_generator("big_file.txt")
row_count = 0
for row in csv_gen:
    row_count += 1
print(f"Row count is {row_count}")
print("TOTAL_TIME:", time.time() - start_time)

print("\nNot using generator...")
start_time = time.time()
csv_gen = csv_reader_not_generator("big_file.txt")
row_count = 0
for row in csv_gen:
    row_count += 1
print(f"Row count is {row_count}")
print("TOTAL_TIME:", time.time() - start_time)
