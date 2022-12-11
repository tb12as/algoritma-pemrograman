# Symetric difference (yang hanya menjadi satu anggota group)
mahasiswa = set(['Andika', 'Jaya', 'Nanda', 'Andyka', 'Fajar', 'Pratama', 'Diana', 'Dwi', 'Apita'])
mhs = {'Nanda', 'Ikhwanul', 'Nandlirin', 'Fajar', 'Ulfah', 'Dwi', 'Nazaria'}

print('Nama bahasiswa yang ikut dalam satu group saja')
print(mahasiswa.symmetric_difference(mhs))

