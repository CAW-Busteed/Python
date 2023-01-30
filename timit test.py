import timeit

# print addition of first 1 million numbers
def addition():
    print('Addition:', sum(range(1000000)))

# run same code 5 times to get measurable data
n = 5

# calculate total execution time
result = timeit.timeit(stmt='addition()', globals=globals(), number=n)

# calculate the execution time
# get the average execution time
print(f"Execution time is {result / n} seconds")