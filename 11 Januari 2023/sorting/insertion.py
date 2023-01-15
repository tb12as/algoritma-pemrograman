def insertion_sort(arr):
    for i in range(1, len(arr)):
        item = arr[i]  # item yang akan diposisikan
        j = i - 1  # index data sebelum item yang akan diposisikan
        # arr[j] = data sebelum data yang akan diposisikan
        while j >= 0 and item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = item
        if __name__ == '__main__':
            print(arr)
    return arr


if __name__ == '__main__':
    print('Final result', insertion_sort([12, 38, 12, 2, 80, 3]))
