def selection_sort(arr):
    length = len(arr)
    count = 0
    for i in range(length):
        min_i = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_i]:
                min_i = j
            count += 1
            print(count, arr)
        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr


print(selection_sort([12, 38, 12, 2, 80, 3]))
# print(selection_sort([1, 3, 5, 2, 45, 12, 99, 10, 33, 0]))
