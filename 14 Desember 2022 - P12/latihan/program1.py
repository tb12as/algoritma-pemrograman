def factorial(numb):
    result = 1
    for x in range(1, numb + 1):
        result *= x

    return result


x = int(input('Masukkan angka yang akan di faktorialkan : '))
print(factorial(x))
