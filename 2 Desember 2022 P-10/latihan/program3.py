row = int(input('Masukkan angka untuk membentuk segitiga : '))
r = 1
while (r <= row):
    for i in range(1, r + 1):
        print(' *', end='')
    print('')
    r += 1
