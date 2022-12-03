nama_mhs = ['Syafiq Afifuddin', 'Nararena Ihsan Maulana', 'Muhammad Ilham Yumar', 'Charolina Novene Marimbunna', 'Zella Syalaisha',
            'Yoga Pradana', 'M Fariq Arib Akbar', 'M Fackhry WT', 'Meirlansyah Rangga', 'Naufal Fadhil Mabrul', 'Harun Al Rasyid']
nim = [3202216080, 3202216082, 3202216084, 3202216115, 3202216124,
       3202216126, 3202216127, 3202216128, 3202216131, 3202216132, 3202216133]
jenis_kelamin = ['Laki-laki', 'Laki-laki', 'Laki-laki', 'Perempuan', 'Perempuan',
                 'Laki-laki', 'Laki-laki', 'Laki-laki', 'Laki-laki', 'Laki-laki', 'Laki-laki']
usia = [19, 18, 17, 17, 18, 17, 17, 18, 18, 17, 17]
header = ['Nama Mahasiswa', 'NIM', 'Jenis Kelamin', 'Usia']

print(f'{header[0]:30} {header[1]:>10} {header[2]:>20} {header[3]:>10}')
for i in range(len(nama_mhs)):
    print(f'{nama_mhs[i]:30} {nim[i]:10} {jenis_kelamin[i]:>20} {usia[i]:>10}')
