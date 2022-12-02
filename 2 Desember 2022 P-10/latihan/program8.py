row = int(input('Masukkan angka untuk membentuk segitiga : '))
r = 1
while (r <= row):
    # print(batas_kiri)
    for c in range(1, row * 2):
        if (c >= r and c <= row * 2 - r):
            # print(f'{c} ', end='')
            print('* ', end='')
        else:
            print('  ', end='')
    print('')
    r += 1
