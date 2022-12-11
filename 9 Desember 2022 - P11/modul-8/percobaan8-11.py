mahasiswa = set(['Andika', 'Jaya', 'Nanda', 'Andyka', 'Fajar', 'Pratama', 'Diana', 'Dwi', 'Apita'])
mhs = {'Nanda', 'Ikhwanul', 'Nandlirin', 'Fajar', 'Ulfah', 'Dwi', 'Nazaria'}
print('Kelompok 1 : \n', mahasiswa)
print('Kelompok 2 : \n', mhs)
print('\n')

# menggunakan simbol - untuk difference
print('>>> menggunakan simbol - untuk difference')
print(mahasiswa - mhs)
print('\n')

# menggunakan fungsi difference
print('>>> menggunakan fungsi difference')
print(mahasiswa.difference(mhs))
print('\n')

