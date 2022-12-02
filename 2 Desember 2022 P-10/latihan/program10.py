row = int(input('Masukkan angka untuk membentuk segitiga : '))
r = 1
while (r <= row * 2 - 1):
    for c in range(1, row * 2):
        if r <= row:
            if (c >= r and c <= (row * 2) - r):
                # print(f' {c} ', end='')
                print(' *', end='')
            else:
                print('  ', end='')
        else:
            if (c > row - (r - row + 1) and c < row + (r - row + 1)):
                # print(f' {c}', end='')
                print(' *', end='')
            else:
                print(f'  ', end='')
    print('')
    r += 1
