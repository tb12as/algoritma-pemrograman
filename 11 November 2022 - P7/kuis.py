print('KUIS MENGHITUNG NILAI MAHASISWA')

nama = input('Masukkan nama Anda	: ')
nim = input('Masukkan NIM Anda	: ')
quiz = float(input('Masukkan nilai Quiz 	: '))
tugas = float(input('Masukkan nilai Tugas	: '))
uts = float(input('Masukkan nilai UTS	: '))
uas = float(input('Masukkan nilai UAS	: '))

print('\n============================================================')
print('            **** KARTU HASIL STUDI MAHASISWA ****           ')
print('============================================================')

print('\nNama Mahasiswa 		: ', nama)
print('NIM Mahasiswa 		: ', nim)
print('Mata Kuliah 		:  Algoritma Pemrograman')
print('Semester / Kelas 	:  I/C')
print('SKS 			:  3 SKS')

print('\nNilai Quiz 		: ', quiz)
print('Nilai Tugas 		: ', tugas)
print('Nilai UTS 		: ', uts)
print('Nilai UAS 		: ', uas)

print('------------------------------------------------------------')
nilai_akhir = (quiz * 10/100) + (tugas * 20/100) + (uts * 30/100) + (uas * 40 / 100)
# 80,51-100 = A, 65,51-80,50 = B, 50,51-65,50 = C, 40,41-50,50 = D, 0,00 - 34,40 = E
if (nilai_akhir >= 80.51 and nilai_akhir <= 100) :
	nilai_huruf = 'A'
elif (nilai_akhir >= 65.51 and nilai_akhir <= 80.50) :
	nilai_huruf = 'B'
elif (nilai_akhir >= 50.51 and nilai_akhir <= 65.50) :
	nilai_huruf = 'C'
elif (nilai_akhir >= 40.51 and nilai_akhir <= 55.50) :
	nilai_huruf = 'D'
elif (nilai_akhir >= 0 and nilai_akhir <= 40.50):
	nilai_huruf = 'E'
else :
	nilai_huruf = 'Ups? Something is wrong'

if nilai_huruf in ['A', 'B', 'C']:
	lulus = 'Lulus'
else:
	lulus = 'Tidak Lulus'

print('Nilai Akhir 		: ', nilai_akhir)
print('Nilai Huruf 		: ', nilai_huruf)
print('Kelulusan 		: ', lulus)

print('\n============================================================')
print('     **** Program Studi D3 Teknik Informatika ****       ')
print('      Jurusan Teknik Elektro Politeknik Negeri Pontianak     ')
print('============================================================')

