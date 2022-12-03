row = int(input('Masukkan angka untuk membentuk segitiga : '))
r = 1
while (r <= row):
    col = row
    while (col > 0):
        if col <= r:
            print(' *', end='')
        else:
            print('  ', end='')
        col -= 1

    print('')
    r += 1
