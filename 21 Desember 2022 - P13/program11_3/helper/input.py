def int_input(message):
    x = input(message)
    if (x.isnumeric() is False):
        print("Input harus berupa angka")
        return int_input(message)

    return int(x)


def float_input(message):
    try:
        return float(input(message))

    except Exception:
        print("Input harus berupa angka")
        return float_input(message)


if __name__ == '__main__':
    print(int_input('Ini integer input : '))
    print(float_input('Ini flaot input : '))
