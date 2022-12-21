def pascal(n):
    result = [[1]]
    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(result[x - 1][y - 1] + result[x - 1][y])
        row.append(1)
        result.append(row)
    return result


n = int(input('Input angka : '))
for v in pascal(n):
    print(v)
