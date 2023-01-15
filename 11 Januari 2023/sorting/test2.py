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
reversed_ordered_list = list(reversed(ordered_list))

lists = {
    'random': random_list,
    'ordered': ordered_list,
    'reversed_ordered': reversed_ordered_list,
}
sorting = ['bubble_sort', 'insertion_sort', 'selection_sort', 'quick_sort']
for sort in sorting:
    print('')
    for k in lists:
        data = [*lists[k]]
        start_time = time.process_time()
        eval(sort + '(' + str(data) + ')')
        time_used = round((time.process_time() - start_time) * 1000, 3)
        print(f'{sort} {k}', time_used, "ms")
