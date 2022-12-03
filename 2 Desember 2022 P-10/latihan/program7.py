row = int(input('Masukkan angka untuk membentuk segitiga : '))
r = 0
while (r < row):
    col = (row * 2) - 1
    while (col > 0):
        # print(r, end='')
        batas_kiri = row + r
        batas_kanan = row - r
        if (col <= batas_kiri and col >= batas_kanan):
            # print(f'{col} ', end='')
            print('* ', end='')
        else:
            print('  ', end='')
        col -= 1

    print('')
    r += 1
