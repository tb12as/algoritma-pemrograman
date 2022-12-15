def intInput(message):
    x = input(message)
    if (x.isnumeric()):
        return int(x)

    print('Input harus berupa angka!')
    return intInput(message)


z = intInput('Masukkan angka : ')
