def angka_tampil(batas, i=1):
    prefix = '--' * (i - 1)
    print(f'{prefix} sebelum rekursif({i})')
    if (i < batas):
        angka_tampil(batas, i + 1)

    print(f'{prefix} setelah rekursif({i})')


angka_tampil(10)
