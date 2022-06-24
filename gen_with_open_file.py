import time


def csv_reader_not_generator(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")


def csv_reader_generator(file_name):
    # create a generator
    with open(file_name, "r") as f:
        for row in f:
            yield row


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
