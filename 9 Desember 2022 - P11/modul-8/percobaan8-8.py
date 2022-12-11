kumpulan = {'manggis', 'mangga', 150, ('x', 'y'), False, True}
print(kumpulan)

# remove, akan error ketika value tidak terdapat dalam list
kumpulan.remove(150)
print(kumpulan)

# kumpulan.remove(200)

# discard, tidak akan error ketika value tidak terdapat dalam list
kumpulan.discard(('x', 'y'))
print(kumpulan)

# pop, menghapus dari sebelah kiri
kumpulan.pop()
print(kumpulan)


# clear, menghapus semua isi set
kumpulan.clear()
print(kumpulan)

