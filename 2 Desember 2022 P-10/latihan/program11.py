n = int(input('Masukkan limit ke-n fibonacci : '))
n1, n2 = 0, 1
i = 0
while (i <= n):
    if i == 0:
        hasil = 0
    elif i == 1 or i == 2:
        hasil = 1
    else:
        hasil = n1 + n2
    n1 = n2
    n2 = hasil
    print(f'fibonacci({i}) = {hasil}')
    i += 1
