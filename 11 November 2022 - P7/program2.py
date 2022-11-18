# https://youtu.be/o4XveLyI6YU
# https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
# https://stackoverflow.com/questions/8347048/how-to-convert-string-to-title-case-in-python
# https://docs.python.org/3/library/stdtypes.html#str.replace
# https://www.geeksforgeeks.org/how-to-capitalize-first-character-of-string-in-python/
# https://www.adamsmith.haus/python/answers/how-to-call-a-function-by-its-name-as-a-string-in-python
# https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key

from math import sqrt
options = [
    'Kubus',
    'Limas Segiempat',
    'Balok',
    'Kerucut',  # Selimut
    'Bola',
    'Tabung',  # Selimut
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


def fixCase(str):
    tmp = str.replace('_', ' ')
    return tmp[0].upper() + tmp[1:]


def execute(fn):
    try:
        fname = fn.title().replace(' ', '')
        fname = fname[0].lower() + fname[1:]
        return eval(fname + '()')
    except Exception:
        # undefined function
        return None


def kubus():
    sisi = floatOrExit(input('\nMasukkan panjang rusuk kubus : '))
    return {'volume': sisi ** 3, 'luas_permukaan': (sisi ** 2) * 6}


def limasSegiempat():
    sisi = floatOrExit(input('\nMasukkan panjang sisi limas : '))
    t = floatOrExit(input('Masukkan tinggi limas : '))
    volume = 1 / 3 * sisi * sisi * t
    luas_segi_3 = (sisi * sqrt(((sisi / 2)**2) + (t ** 2))) / 2
    luas_permukaan = (sisi ** 2) + (4 * luas_segi_3)

    return {'volume': volume, 'luas_permukaan': luas_permukaan}


def balok():
    p = floatOrExit(input('\nMasukkan panjang balok : '))
    lebar = floatOrExit(input('Masukkan lebar balok : '))
    t = floatOrExit(input('Masukkan tinggi balok : '))
    volume = p * lebar * t
    luas_permukaan = 2 * ((p * lebar) + (lebar * t) + (p * t))
    return {'volume': volume, 'luas_permukaan': luas_permukaan}


def kerucut():
    r = floatOrExit(input('\nMasukkan panjang jari-jari alas kerucut: '))
    t = floatOrExit(input('Masukkan tinggi kerucut : '))
    v = 3.14 * r * r * t
    luas_permukaan = 3.14 * r * (r + sqrt(r * r + t * t))
    luas_selimut = 3.14 * r * sqrt(r * r + t * t)
    return {
        'volume': v,
        'luas_permukaan': luas_permukaan,
        'luas_selimut': luas_selimut
    }


def bola():
    r = floatOrExit(input('\nMasukkan panjang jari-jari bola : '))
    v = 4 / 3 * 3.14 * r ** 3
    luas_permukaan = 4 * 3.14 * r ** 2
    return {'volume': v, 'luas_permukaan': luas_permukaan}


def tabung():
    r = floatOrExit(input('\nMasukkan panjang jari-jari tabung : '))
    t = floatOrExit(input('Masukkan tinggi tabung : '))
    v = 3.14 * r * r * t
    luas_permukaan = 2 * 3.14 * r * (r + t)
    l_selimut = 2 * 3.14 * r * t
    return {
        'volume': v,
        'luas_permukaan': luas_permukaan,
        'luas_selimut': l_selimut
    }


def start(firstTry):
    while True:
        if (not firstTry):
            repeat = input(
                '\nHitung bangun ruang yang lain? [ya, tidak] ')
            if repeat.lower() in ('ya', 'tidak'):
                if (repeat.lower() == 'tidak'):
                    break
            else:
                print("Pilihan hanya ya atau tidak")
                start(False)
                break

        for i in range(len(options)):
            print(f"{i + 1}. {options[i]}")

        select = input('Pilih bangun ruang : ')
        if select != '' and select.isdigit():
            index = int(select) - 1
        else:
            break

        if select != '' and index in range(len(options)):
            firstTry = False
            selected = options[index].lower()
            result = execute(selected)
            if result:
                for key, value in result.items():
                    # powers = "3" if key == 'volume' else "2"
                    powers = "2"
                    ln = ''
                    if key == 'volume':
                        powers = "3"
                        ln = '\n'

                    key = fixCase(key)
                    print(
                        f"{ln}{key} {selected} : {value} cm^" + powers)
        else:
            print('Pilihan tidak ditemukan')


start(True)
