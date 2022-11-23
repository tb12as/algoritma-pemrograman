def intInput(message):
    number = input(message)
    if (number.isnumeric()):
        return int(number)
    else:
        print('Input harus berupa angka!')
        return intInput(message)


angka1 = intInput("Masukkan angka 1 : ")
angka2 = intInput("Masukkan angka 2 : ")
if (angka1 > angka2):
    print(f'{angka1} lebih besar dari {angka2}')
elif (angka1 == angka2):
    print(f'{angka1} sama dengan {angka2}')
else:
    print(f'{angka1} lebih kecil dari {angka2}')
