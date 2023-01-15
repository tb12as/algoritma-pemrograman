# https://www.geeksforgeeks.org/python-reversing-list/

import time
from selection import *
from bubble import *
from insertion import *
from quick_sort import *

random_list = [100, 21, 33, 19, 5, 23, 41, 30, 18, 7, 92, 43, 78, 29, 16, 82,
               12, 81, 36, 79, 22, 8, 1, 11, 86, 52, 89, 32, 53, 83, 54, 69,
               25, 77, 73, 47, 61, 28, 51, 99, 66, 15, 42, 88, 37, 76, 31, 62,
               87, 74, 58, 46, 39, 75, 38, 48, 63]
ordered_list = quick_sort([*random_list])
reversed_ordered_list = list(reversed([*ordered_list]))

# bubble sort
start_time = time.process_time()
bubble_sort([*random_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'{"Bubble sort random list":40}', time_used, "ms")

start_time = time.process_time()
bubble_sort([*ordered_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'{"Bubble sort orderd list":40}', time_used, "ms")

start_time = time.process_time()
bubble_sort([*reversed_ordered_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'{"Bubble sort reversed orderd list":40}', time_used, "ms")


# selection sort
start_time = time.process_time()
selection_sort([*random_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'\n{"Selection sort random list":40}', time_used, "ms")

start_time = time.process_time()
selection_sort([*ordered_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'{"Selection sort orderd list":40}', time_used, "ms")

start_time = time.process_time()
selection_sort([*reversed_ordered_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'{"Selection sort reversed orderd list":40}', time_used, "ms")

# insertoin sort
start_time = time.process_time()
insertion_sort([*random_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'\n{"Insertion sort random list":40}', time_used, "ms")

start_time = time.process_time()
insertion_sort([*ordered_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'{"Insertion sort orderd list":40}', time_used, "ms")

start_time = time.process_time()
insertion_sort([*reversed_ordered_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'{"Insertion sort reversed orderd list":40}', time_used, "ms")


# quick sort
start_time = time.process_time()
quick_sort([*random_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'\n{"Quick sort random list":40}', time_used, "ms")

start_time = time.process_time()
quick_sort([*ordered_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'{"Quick sort orderd list":40}', time_used, "ms")

start_time = time.process_time()
quick_sort([*reversed_ordered_list])
time_used = round((time.process_time() - start_time) * 1000, 3)
print(f'{"Quick sort reversed orderd list":40}', time_used, "ms")

# print(len(random_list))
# print(quick_sort(random_list))
# print(random_list)
# print(len(random_list))
