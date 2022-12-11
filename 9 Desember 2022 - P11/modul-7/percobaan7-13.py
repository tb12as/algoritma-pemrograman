baris_angka = [-1, 3, 17, 14, 11, 6, 18, 93, 88, 20, 16, 17]
print(baris_angka)

bil_genap = [genap for genap in baris_angka if genap % 2 == 0]
print(f'Jumlah bilangan genap {len(bil_genap)} angka, yaitu : {bil_genap}')

bil_ganjil = [ganjil for ganjil in baris_angka if ganjil % 2 != 0]
print(f'Jumlah bilangan ganjil {len(bil_ganjil)} angka, yaitu : {bil_ganjil}')

