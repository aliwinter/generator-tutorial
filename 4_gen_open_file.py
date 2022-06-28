import time
import pandas as pd

def csv_reader_not_generator(file_name):
    result = []
    with open(file_name, "r") as f:
        for row in f.read().split("\n"):
            result.append(row)
    return result


def csv_reader_generator(file_name):
    # open(file_name, "r") -> returns a generator
    f = open(file_name, "r")
    for row in f:
        row = row.split(",")
        yield row  # returns a generator object
    f.close()


print("\n Not using generator...")
start_time = time.time()
csv_gen = csv_reader_not_generator("big_file.txt")
row_count = 0
for row in csv_gen:
    row_count += 1
print(f"Row count is {row_count}")
print("TOTAL_TIME:", time.time() - start_time)


print("Using generator...")
start_time = time.time()
csv_gen = csv_reader_generator("big_file.txt")
new_csv_gen = [x + ", new_feature" for x in csv_gen]
row_count = 0
for row in new_csv_gen:
    row_count += 1
print(f"Row count is {row_count}")
print("TOTAL_TIME:", time.time() - start_time)


# Load Generator object into a dataframe
# generatorObject = csv_reader_generator("big_file.txt")
# df = pd.DataFrame(generatorObject)
# print(df.head())
