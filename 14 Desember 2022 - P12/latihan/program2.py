import string


def countCase(str):
    strings = [v for v in list(str) if v.lower() in string.ascii_lowercase]
    upper = [v for v in strings if v.isupper()]

    return {
        'upper_case': len(upper),
        'lower_case': len(strings) - len(upper)
    }


result = countCase('Ani dan Budi belajar di rumah Joko, di Desa Suka Maju')
print(f'Jumlah karakter uppercase pada string : {result["upper_case"]}')
print(f'Jumlah karakter lowercase pada string : {result["lower_case"]}')
