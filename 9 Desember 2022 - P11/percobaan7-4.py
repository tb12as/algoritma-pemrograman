list1 = ['Teknik informatika', 'Teknik Elektro', 2009, 2012]
list2 = [3, 20, 22, 16, 150]
list3 = ['C', 'B', 'Sangat Baik', 'Unggul']

print('Nilai list sebelum ditambah')
print('list1 >>>', list1)
print('list2 >>>', list2)
print('list3 >>>', list3)

# Menambah list dengan insert
print('Nilai list1 setelah ditambah  dengan fungsi insert')
list1.insert(0, 'Teknolog Informasi')
print(list1)

print('Nilai list2 setelah ditambah dengan fungsi insert')
list2.insert(3, 300)
print(list2)

# Menambah list dari akhir dengan fungsi append
print('Niali list3 setelah ditambah dengan fungsi append')
list3.append('A')
print(list3)



