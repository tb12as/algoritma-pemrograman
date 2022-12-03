row = int(input('Masukkan angka untuk membentuk segitiga : '))
while (row > 0):
    for i in range(1, row + 1):
        print(' *', end='')
    print('')
    row -= 1
