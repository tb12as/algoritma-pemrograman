# String ke numeric
a = '5'
b = '10'

# print(a * b) # akan error
print(int(a) * int(b))
print(float(a))

# Numeric ke string
print("-" * 30)
name = 'Syafiq'
tahun_lahir = 2002
# print(name + ' lahir pada tahun ' + tahun_lahir)  # akan error
print(name + ' lahir pada tahun ' + str(tahun_lahir))


# Konversi ke boolean
print("-" * 30)
print(type(None), '->', bool(None))
print(type(0), '->', bool(0))
print(type(0.0), '->', bool(0.0))
print(type(""), '->', bool(""))
print(type([]), '->', bool([]))
print(type(()), '->', bool(()))
print(type({}), '->', bool({}))

print("-" * 30)

print(type(5), '->', bool(5))
print(type(-14.5), '->', bool(-14.5))
print(type("Aku"), '->', bool("Aku"))
print(type([1, 2, 3]), '->', bool([1, 2, 3]))
print(type(("a", "b", False)), '->', bool(("a", "b", False)))
print(type({'nama': 'Lendis Fabri'}), '->', bool({'nama': 'Syafiq'}))

# Konversi Dari dan Ke List, Set dan Tuple
print("-" * 30)
# list ke tuple dan ke set
listHuruf = ['a', 'b', 'c', 'c']
print(listHuruf)
print(tuple(listHuruf))
print(set(listHuruf))

# tuple ke list dan ke set
print("-" * 30)
tplBuah = ('Mangga', 'Jambu')
print(tplBuah)
print(list(tplBuah))
print(set(tplBuah))
