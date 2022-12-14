def multipy_list(x, y):
    result = []
    for v in range(x, y):
        result.append(v * v)

    return result


x = int(input('Awal range : '))
y = int(input('Akhir angka sebelum : '))
print(multipy_list(x, y))
