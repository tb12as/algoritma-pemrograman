original_string = 'Pada hari Senin, Saya Belajar Mata Kuliah Algoritma Pemrograman di Kelas TI-A Gedung Teori Jurusan Teknik Elektro Program Studi D3 Teknik Informatika pada Pukul 07.00 WIB sampai dengan 14.40 WIB.'

#print(original_string.split(' '))
result = [val for val in original_string.split(' ') if len(val.replace(',', '')) > 5]
print('Kata yang lebih dari 4 huruf adalah :', result)

