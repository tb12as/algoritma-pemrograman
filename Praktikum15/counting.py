def counting_sort(arr):
    n = len(arr)
    m = max(arr) + 1
    count = [0] * m
    output = [0] * n

    for i in range(n):
        count[arr[i]] += 1

    for i in range(1, m):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output
