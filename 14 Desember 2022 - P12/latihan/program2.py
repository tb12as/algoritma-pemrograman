import string


def countCase(str):
    strings = [v for v in list(str) if v.lower() in string.ascii_lowercase]
    upper = [v for v in strings if v.isupper()]

    return {
        'upper_case': len(upper),
        'lower_case': len(strings) - len(upper)
    }


print(countCase('Ani dan Budi belajar di rumah Joko, di Desa Suka Maju'))
