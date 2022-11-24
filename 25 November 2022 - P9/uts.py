def isInt(num):
    try:
        int(num)
        return True
    except Exception:
        return False


def intInput(message):
    value = input(message)
    if(isInt(value)):
        return int(value)
    else:
        print('Input harus berupa angka!')
        return intInput(message)


test = intInput('Masukkan angka : ')
print(test)
