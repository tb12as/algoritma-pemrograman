# OR (return 1 if bin(a)[i] == 1 || bin(b)[i] == 1)
a = 75
b = 82
print(f'Nilai biner dari a yaitu {a} adalah : ' + format(a, '08b'))
print(f'Nilai biner dari b yaitu {b} adalah : ' + format(b, '08b'))

print('\nNilai a OR b : ' + str(a | b))
print('Nilai biner dari a OR b adalah : ' + format(a | b, '08b'))

# AND (return 1 if bin(a)[i] == 1 && bin(b)[i] == 1)
a = 114;
b = 218;
print('\nNilai a AND b : ' + str(a & b))
print('Nilai biner dari a AND b adalah : ' + format(a & b, '08b'))

# XOR (return 1 if bin(a)[i] != bin(b)[i])
a = 13;
b = 4;
print('\nNilai a XOR b : ' + str(a ^ b))
print('Nilai biner dari a XOR b adalah : ' + format(a ^ b, '08b'))

# NOT (swap 1 to 0, 0 to 1)
a = 91
b = 82
print('\nNilai ~a : ' + str(~a) + ' dan Nilai dari ~b adalah : ' + str(~b))
print('Nilai biner dari ~a adalah : ' + format(~a, '08b'))
print('Nilai biner dari ~b adalah : ' + format(~b, '08b'))
