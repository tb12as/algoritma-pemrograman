mahasiswa = set(['Andika', 'Jaya', 'Nanda', 'Andyka', 'Fajar', 'Pratama', 'Diana', 'Dwi', 'Apita'])
mhs = {'Nanda', 'Ikhwanul', 'Nandlirin', 'Fajar', 'Ulfah', 'Dwi', 'Nazaria'}
print('Kelompok 1 : \n', mahasiswa)
print('Kelompok 2 : \n', mhs)
print('\n')

# cara 1 menggunakan simbol &
print('>>> intersection menggunakan simbol &')
print(mahasiswa & mhs)
print('\n')

# cara 2 menggunakan fungsi intersection
print('>>> menggunakan fungsi intersection')
print(mahasiswa.intersection(mhs))
print('\n')


