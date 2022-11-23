# https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import datetime


def intInput(message):
    number = input(message)
    if (number.isnumeric()):
        return int(number)
    else:
        print('Input harus berupa angka!')
        return intInput(message)


namaToko = 'Polnep Mart'
alamatToko = 'Jl. Jenderal Ahmad Yani'
today = datetime.now()
tanggal = today.strftime('%d-%m-%Y, %H:%M:%S')
namaKasir = 'Syafiq Afifuddin'
namaPelanggan = input('Masukkan nama pelanggan : ')

total = intInput('Masukkan total belanjaan : ')
if (total > 250000):
    diskon = 15
elif (total >= 150000):
    diskon = 10
elif (total > 50000):
    diskon = 5
else:
    diskon = 0

totalDiskon = (total * diskon / 100)
totalBayar = total - totalDiskon

print('\n')
print('========================================')
print(f'              {namaToko}              ')
print(f'       {alamatToko}       ')
print(f'        {str(tanggal)}')
print('========================================')
print(f'Nama Pelanggan      : {namaPelanggan}')
print(f'Nama Kasir          : {namaKasir}')
if (diskon > 0):
    print(f'Selamat Anda mendapat diskon sebesar {diskon}%')
print(f'Total Belanja       : {total}')
print(f'Potongan Harga      : {totalDiskon}')
print(f'Total Bayar         : {totalBayar}')
print(f'\nTerima kasih sudah belanja di {namaToko}')
