
def bubble_sort(array):
    n = len(array)  # jumlah list
    # perulangan pertama
    x = 0
    for i in range(n):
        # perulangan kedua
        for j in range(n - i - 1):
            # bandingkan masing-masing elemen
            if array[j] > array[j + 1]:
                # jika lebih besar, tukar.
                array[j], array[j + 1] = array[j + 1], array[j]

            x += 1
            print(array, x, '  ', j, j + 1)

    return array


result = bubble_sort([12, 38, 12, 2, 80, 3])
# for v in result:
#     print(v)
