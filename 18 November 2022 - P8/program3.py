def intInput(message):
    number = input(message)
    if (number.isnumeric()):
        return int(number)
    else:
        print('Input harus berupa angka!')
        return intInput(message)


age = intInput('Masukkan umur : ')
if (age > 60):
    status = 'Lansia'
elif (age > 30):
    status = 'Dewasa'
elif (age > 17):
    status = 'Muda'
elif (age > 12):
    status = 'Remaja'
elif (age > 5):
    status = 'Anak-anak'
else:
    status = 'Balita'

print(f'Usia {age} adalah {status}')
