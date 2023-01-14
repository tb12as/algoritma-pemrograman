def bubble_sort(array):
    n = len(array)  # jumlah list
    # perulangan pertama
    count = 0
    for i in range(n):
        # perulangan kedua
        for j in range(n - i - 1):
            count += 1
            # urutan : array, iterasi, index yg dibandingkan, data
            print(
                array, f'{count:2}   {j:2} {(j+1):2}    {array[j]:2} {array[j+1]:2}')
            # bandingkan masing-masing elemen
            if array[j] > array[j + 1]:
                # jika lebih besar, tukar.
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


result = bubble_sort([12, 38, 12, 2, 80, 3])
print("Result : ", result)
