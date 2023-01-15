# https://stackoverflow.com/questions/45708626/read-data-in-excel-column-into-python-list
# https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
# https://www.geeksforgeeks.org/creating-a-dataframe-using-excel-files/
# https://bobbyhadz.com/blog/python-check-if-index-exists-in-list
# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

import pandas as pd
import numpy as np
import itertools
from selection import *
from bubble import *
from insertion import *
from quick_sort import *

# get nim only from the excel file
df = pd.read_excel('data.xlsx', usecols=[1], sheet_name=None, header=4)

# transform nim from each sheet to one list
nim = []
for sheet in df:
    data = df[sheet]['NIM'].values.tolist()
    nim.append(data)

# flatten the list and sort it
nim = list(itertools.chain(*nim))
# nim = bubble_sort(nim)
# nim = selection_sort(nim)
# nim = insertion_sort(nim)
nim = quick_sort(nim)

# chunk to 5 and print the elements from each chunk at the same i index.
# full screen terminal / cmd are recommended
chunk_length = 5
chunked_nim = np.array_split(nim, chunk_length)
max_length = len(chunked_nim[0])
for i in range(max_length):
    for j in range(chunk_length):
        if len(chunked_nim[j]) - 1 >= i:
            print(chunked_nim[j][i], end='  ')
    print('')

# if you want unchunked nim, you can use this variable
# print(nim)
