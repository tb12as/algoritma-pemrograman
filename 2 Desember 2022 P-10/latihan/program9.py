row = int(input('Masukkan angka untuk membentuk belah ketupat : '))
r = 1
while (r <= row * 2 - 1):
    for c in range(1, row * 2):
        if r <= row - 1:
            if (c > row - r and c < row + r):
                # print(f'{c} ', end='')
                print(' * ', end='')
            else:
                print(f'   ', end='')
        else:
            batas_kiri = r - (row - 1)
            batas_kanan = (row * 2) - batas_kiri

            if (c >= batas_kiri and c <= batas_kanan):
                # print(f'{c} ', end='')
                print(' * ', end='')
            else:
                print('   ', end='')
    print('')
    r += 1
