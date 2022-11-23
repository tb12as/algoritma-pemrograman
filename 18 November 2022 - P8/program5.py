# https://science.howstuffworks.com/science-vs-myth/everyday-myths/question50.htm

def intInput(message):
    number = input(message)
    if (number.isnumeric()):
        return int(number)
    else:
        print('Input harus berupa angka!')
        return intInput(message)


name = 'Syafiq Afifuddin'
date = 12
month = 'Desember'

year = intInput('Masukkan tahun : ')
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(
        f'Saudara {name} Anda lahir pada {date} {month} {year}. Anda lahir di tahun kabisat')

else:
    print(
        f'Saudara {name} Anda lahir pada {date} {month} {year}. Anda lahir bukan di tahun kabisat')
