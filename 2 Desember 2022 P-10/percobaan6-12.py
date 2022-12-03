nama_mhs = ['Nuraini Putri Cahrulina',
            'Siti Sabrina Oktavia', 'Adil Fathi Abdillah']
nim = [3202216001, 3202216002, 3202216005]
jenis_kelamin = ['Perempuan', 'Perempuan', 'Laki-laki']
usia = [18, 19, 17]
header = ['Nama Mahasiswa', 'NIM', 'Jenis Kelamin', 'Usia']

print(f'{header[0]:30} {header[1]:>10} {header[2]:>20} {header[3]:>10}')

for i in range(len(nama_mhs)):
    print(f'{nama_mhs[i]:30} {nim[i]:10} {jenis_kelamin[i]:>20} {usia[i]:>10}')
