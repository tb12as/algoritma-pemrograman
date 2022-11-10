# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
# https://pynative.com/python-check-user-input-is-number-or-string/
# https://www.programiz.com/python-programming/for-loop
# https://stackoverflow.com/questions/18863309/the-equivalent-of-a-goto-in-python
# https://rollbar.com/blog/throwing-exceptions-in-python/
# https://www.programiz.com/python-programming/examples/check-string-number

options = [
    'Persegi',
    'Persegi panjang',
    'Jajar genjang',
    'Trapesium', 
    'Belah ketupat',
    'Layang-layang',
    'Segitiga',
    'Lingkaran'
]

def isFloat(n):
    try:
        float(n)
        return True

    except ValueError:
        return False

def floatOrExit(str):
    try:
        assert(isFloat(str)), "Error : Input harus berupa angka"
        return float(str)
    except Exception as e:
        print(e)
        exit()

def persegi():
    sisi = input('\nMasukkan sisi persegi : ')
    sisi = floatOrExit(sisi)

    return {'luas' : sisi ** 2, 'keliling' : sisi * 4}

def persegiPanjang():
    panjang = floatOrExit(input('\nMasukkan panjang persegi panjang : '))
    lebar = floatOrExit(input('Masukkan lebar persegi panjang : '))

    return {'luas' : panjang * lebar, 'keliling' : (panjang + lebar) * 2}

def jajarGenjang():
    alas = floatOrExit(input('\nMasukkan panjang alas jajar genjang : '))
    tinggi = floatOrExit(input('Masukkan tinggi jajar genjang : '))
    miring = floatOrExit(input('Masukkan panjang sisi miring jajar genjang : '))

    return {'luas' : alas * tinggi, 'keliling' : (alas + miring) * 2}

def trapesium():
    a = floatOrExit(input('Masukkan sisi sejajar 1 (a) trapesium : '))
    b = floatOrExit(input('Masukkan sisi sejajar 2 (b) trapesium : '))
    h = floatOrExit(input('Masukkan tinggi (h) trapesium : '))
    miring1 = floatOrExit(input('Masukkan panjang sisi miring 1 : '))
    miring2 = floatOrExit(input('Masukkan panjang sisi miring 2 : '))

    luas = 1/2 * (a+b) * h
    keliling = a + b + miring1 + miring2

    return {'luas' : luas, 'keliling' : keliling}

def belahKetupat():
    sisi = floatOrExit(input('\nMasukkan panjang sisi belah ketupat : '))
    diagonal1 = floatOrExit(input('Masukkan panjang diagonal 1 belah ketupat : '))
    diagonal2 = floatOrExit(input('Masukkan panjang diagonal 2 belah ketupat : '))

    luas = 1/2 * diagonal1 * diagonal2
    keliling = sisi * 4;
    return {'luas' : luas, 'keliling' : keliling}

def layangLayang():
    diagonal1 = floatOrExit(input('Masukkan panjang diagonal 1 layang-layang : '))
    diagonal2 = floatOrExit(input('Masukkan panjang diagonal 2 layang-layang : '))
    rusuk1 = floatOrExit(input('Masukkan panjang rusuk 1 layang-layang : '))
    rusuk2 = floatOrExit(input('Masukkan panjang rusuk 2 layang-layang : '))

    luas = 1/2 * diagonal1 * diagonal2
    keliling = (rusuk1 + rusuk2) * 2
    return {'luas' : luas, 'keliling' : keliling}

def segitiga():
    alas = floatOrExit(input('Masukkan panjang alas segitiga : '))
    tinggi = floatOrExit(input('Masukkan tinggi segitiga : '))
    sisi1 = floatOrExit(input('Masukkan panjang sisi miring 1 segitiga : '))
    sisi2 = floatOrExit(input('Masukkan panjang sisi miring 2 segitiga : '))

    return {'luas' : 1/2 * alas * tinggi, 'keliling' : alas + sisi1 + sisi2}

def lingkaran():
    r = floatOrExit(input('Masukkan panjang jari-jari lingkaran : '))
    phi = 22 / 7
    return {'luas' : phi * r * r, 'keliling' : 2 * phi * r}

def start(firstTry):
    while True:
        if (firstTry == False):
            repeat = input('\nApakah anda ingin menghitung bangun datar yang lain? ? [ya, tidak] ')
            if repeat.lower() in ('ya', 'tidak'):
                if (repeat.lower() == 'tidak'): break
            else:
                print("Pilihan hanya ya atau tidak")
                start(False)
                break

        for i in range(len(options)):
            no = i + 1;
            print(f"{no}. {options[i]}")

        select = input('Pilih bangun datar : ')
        if select != '' and select.isdigit():
            index = int(select) - 1
        else: break
            
        if select != '' and index in range(len(options)):
            selected = options[index]
            firstTry = False

            if selected == 'Persegi':
                result = persegi()
            elif selected == 'Persegi panjang':
                result = persegiPanjang()
            elif selected == 'Jajar genjang':
                result = jajarGenjang()
            elif selected == 'Belah ketupat':
                result = belahKetupat()
            elif selected == 'Trapesium':
                result = trapesium()
            elif selected == 'Layang-layang':
                result = layangLayang()
            elif selected == 'Segitiga':
                result = segitiga()
            elif selected == 'Lingkaran':
                result = lingkaran()
            else:
                result = None

            if result:
                print(f"\nLuas {selected.lower()} : {result['luas']} cm^2")
                print(f"Keliling {selected.lower()} : {result['keliling']} cm")
        else:
            print('Pilihan tidak ditemukan')

start(True)
