import random
import string
import time

from merge import merge_sort
from heap import heap_sort
from shell import shell_sort
from counting import counting_sort

rand_length = int(input("Masukkan jumlah random list : "))
random_int = [random.randint(1, 1e5) for _ in range(rand_length)]
random_float = [random.random() * 100 for _ in range(rand_length)]
random_str = [''.join(random.choices(string.ascii_letters, k=2))
              for _ in range(rand_length)]

print("Random list length :", rand_length)
# Random int
print("Random Integer")
start = time.process_time()
merge_sort([*random_int])
print(f'{"merge_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")

start = time.process_time()
heap_sort([*random_int])
print(f'{"heap_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")

start = time.process_time()
shell_sort([*random_int])
print(f'{"shell_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")

start = time.process_time()
shell_sort([*random_int])
print(f'{"shell_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")

start = time.process_time()
counting_sort([*random_int])
print(f'{"counting_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")


# Random float
print("\nRandom Float")
start = time.process_time()
merge_sort([*random_float])
print(f'{"merge_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")

start = time.process_time()
heap_sort([*random_float])
print(f'{"heap_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")

start = time.process_time()
shell_sort([*random_float])
print(f'{"shell_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")


# Random float
print("\nRandom String")
start = time.process_time()
merge_sort([*random_str])
print(f'{"merge_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")

start = time.process_time()
heap_sort([*random_str])
print(f'{"heap_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")

start = time.process_time()
shell_sort([*random_str])
print(f'{"shell_sort  ":>20}', round(
    (time.process_time() - start) * 1000, 3), "ms")
