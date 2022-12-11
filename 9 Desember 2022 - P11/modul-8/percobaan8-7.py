# menambah anggota baru pada set denga fungsi add()
print('>>>nilai awal set mata kuliah')
makul = {'Pancasila', 'MTK 1', 'PTI', 'Pemrograman Terstruktur'}
print(makul)

print('>>> menambah set dengan fungsi add')
makul.add('Paket Program Terapan')
print(makul)

# You can't using add function with +1 params
# makul.add('Paket Program Terapan', 'Algoritma Pemrograman')
# print(makul)

# menambah anggota baru pada set menggunakan fungsi update()
print('>>> menambah set dengan fungsi update')
makul.update({'Algoritma Pemrograman', 'Praktikum Pemrograman Terstruktur'})
makul.update({'Praktikum Paket Program Terapan'})
print(makul)


