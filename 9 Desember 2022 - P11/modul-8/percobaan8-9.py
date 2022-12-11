# another useless thing here :
# grup_smp = {'andi', 'budi', 'ratna', 'sari'}
# grup_sma = {'putri', 'ratna', 'andi', 'agus'}


# menggunakan fungsi union
mahasiswa = set(['Andika', 'Jaya', 'Nanda', 'Andyka', 'Fajar', 'Pratama', 'Diana', 'Dwi', 'Apita'])
mhs = {'Nanda', 'Ikhwanul', 'Nandlirin', 'Fajar', 'Ulfah', 'Dwi', 'Nazaria'}
print('Kelompok 1 : \n', mahasiswa)
print('Kelompok 2 : \n', mhs)
print('\n')

# dengan pipe ( | )
print('>>> Cara 1 fungsi union dengan simbol pipe |')
print(mahasiswa | mhs)
print('\n')

# Menggunakan fungsi union
print('>>> Cara 2 menggunakan fungsi union')
print(mahasiswa.union(mhs))
print('\n')


