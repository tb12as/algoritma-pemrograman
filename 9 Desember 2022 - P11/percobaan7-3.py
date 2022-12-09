# Mengupdate nilai dalam list
print('Sebelum melakukan update')
list1 = ['Teknik informatika', 'Teknik Elektro', 2001, 2022]
print('Nilai list pada index 0 adalah ', list1[0])
print('Nilai list pada index 2 adalah ', list1[2])
print('-' * 70)

# Update nilai pada index 1 dan 2
print('Setelah melakukan update')
list1[2] = 2009
list1[0] = 'Teknologi Informasi'
print('Nilai baru pada index 0 sekarang adalah ', list1[0])
print('Nilai baru pada index 2 sekarang adalah ', list1[2])
print('-' * 70)

# Update list dengan dengan range
list1[0:2] = 'D4', 'Rekayasa Perangkat Lunak'

print('Nilai semua setelah diupdate ', list1)


