row = int(input('Masukkan angka untuk membentuk segitiga : '))
r = 1
while (r <= row):
    for i in range(1, row + 1):
        if i >= r:
            print(' *', end='')
        else:
            print('  ', end='')
    print('')
    r += 1
