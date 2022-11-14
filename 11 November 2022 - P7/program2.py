import math
options = [
    'Kubus',
    'Limas Segiempat',
    'Balok',
    'Kerucut', # Selimut
    'Bola',
    'Tabung', # Selimut
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

def kubus():
    sisi = floatOrExit(input('Masukkan panjang rusuk kubus : '))
    return {
        'volume' : sisi ** 3,
        'luas_permukaan': (sisi ** 2) * 6
    }

def limas():
    sisi = floatOrExit(input('Masukkan panjang sisi limas : '))
    t = floatOrExit(input('Masukkan tinggi limas : '))
    volume = 1/3 * sisi * sisi * t;
    luas_segi_3 = (sisi * math.sqrt(((sisi / 2)**2) + (t ** 2))) / 2
    luas_permukaan = (sisi ** 2) + (4 * luas_segi_3)

    return {'volume': volume, 'luas_permukaan': luas_permukaan}

def balok():
    p = floatOrExit(input('Masukkan panjang balok : '));
    l = floatOrExit(input('Masukkan lebar balok : '));
    t = floatOrExit(input('Masukkan tinggi balok : '));

    volume = p * l * t;
    luas_permukaan = 2 * ((p * l) + (l * t) + (p * t))
    return {'volume': volume, 'luas_permukaan': luas_permukaan}

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

            if selected == 'Kubus':
                result = kubus()
            elif selected == 'Limas Segiempat':
                result = limas()
            elif selected == 'Balok':
                result = balok()
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
                print(f"\nVolume {selected.lower()} : {result['volume']} cm^3")
                print(f"Luas Permukaan {selected.lower()} : {result['luas_permukaan']} cm^2")
        else:
            print('Pilihan tidak ditemukan')

start(True)
