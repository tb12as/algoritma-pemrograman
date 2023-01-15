def selection_sort(arr):
    length = len(arr)
    count = 0
    for i in range(length):
        min_i = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_i]:
                min_i = j

            if __name__ == '__main__':
                # format : arr, iteration, index yg dibandingkan, min
                count += 1
                print(arr, f'{count:<2}  {i}-{j} {min_i:2}')
        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr


if __name__ == '__main__':
    print(selection_sort([12, 38, 12, 2, 80, 3]))
