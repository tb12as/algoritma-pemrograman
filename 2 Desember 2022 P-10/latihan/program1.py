angka = list(range(1, 10))
genap = 0
ganjil = 0
for x in angka:
    if (x % 2 == 0):
        genap += 1
    else:
        ganjil += 1

print(f'List angka {angka}')
print(f'Jumlah angka genap {genap}')
print(f'Jumlah angka ganjil {ganjil}')
