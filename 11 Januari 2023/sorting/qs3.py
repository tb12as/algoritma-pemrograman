def partisi(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    print(arr)
    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        pi = partisi(arr, left, right)
        quick_sort(arr, left, pi - 1)
        quick_sort(arr, pi + 1, right)
    return arr


list = [67, 91, 87, 33, 49, 16, 16, 43, 65, 3]
data = quick_sort(list, 0, len(list) - 1)
print('data', data)
