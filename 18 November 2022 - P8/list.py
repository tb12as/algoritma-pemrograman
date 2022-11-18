# Membuat list kosong
list_kosong = []

# Membuat list yang berisi kumpulan string
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian', 'Duku', 'Semangka']

# Membuat list yang berisi kumpulan integer 
list_nilai = [80, 70, 60, 90, 95]

# Membuat list yang berisi kumpulan float
list_ipk = [4.0, 3.81, 3.58, 3.32, 2.89]

# Membuat list campuran berbagai tipe data
list_jawaban = [150, 33.33, 'Presiden Soekarno', False]

# print('list_kosong : ', list_kosong)
# print('list_buah : ', list_buah[0])
# print('list_nilai : ', list_nilai[0])
# print('list_ipk : ', list_ipk[0])
# print('list_jawaban : ', list_jawaban[0])

# print(list_buah[1])
# print(list_buah[2])
# print(list_buah[-1])
# print(list_buah[-2])

# print(list_buah[0:1])
# print(list_buah[0:2])
# print(list_buah[1:3])
# print(list_buah[-2])
# print(list_buah[-3:1])
# print(list_buah[-1:3])
# print(list_buah[-3:-1])

# print(list_buah[0:])
# print(list_buah[1:])
# print(list_buah[2:])
# print(list_buah[3:])
# print(list_buah[4:])
# print(list_buah[5:])
# print(list_buah[6:])

# print(list_buah[:0])
# print(list_buah[:1])
# print(list_buah[:2])
# print(list_buah[:3])
# print(list_buah[:4])
# print(list_buah[:5])
# print(list_buah[:6])

list_buah[0] = 'Mangga'
list_buah[5] = 'Kiwi'
list_buah[1:3] = ['Naga', 'Pepaya']

list_buah.append('Sirsak')
list_buah.insert(0, 'Jambu')
list_buah.insert(2, 'Manggis')
list_buah.insert(6, 'Rambutan')

list_buah.pop(2)
list_buah.remove('Rambutan')

del list_buah[3]
del list_buah[1:3]

# print(list_buah[0:2])
# print(list_buah)
# print(len(list_buah))

# Menggabungkan list
a = [1,2,3]
b = ['a']
c = [True, 'b', False]
d = a + b + c
# print(d)

# Mengurutkan list
# asc = Dari kecil ke besar
# desc = Dari besar ke kecil

list_buah.sort() # default ascending

list_nilai.sort()
list_nilai.reverse()
print(list_nilai)


