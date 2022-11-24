def isInt(num):
    try:
        int(num)
        return True
    except Exception:
        return False


def intInput(message):
    value = input(message)
    if (isInt(value)):
        return int(value)
    else:
        print('Input harus berupa angka!')
        return intInput(message)


def menuInput():
    index = intInput('Pilih menu : ') - 1
    if (index in range(len(menu))):
        return menu[index]
    else:
        print('Menu tidak ditemukan')
        return menuInput()


menu = [
    {'name': 'Apaa', 'price': 5000},
    {'name': 'Kubus', 'price': 51000}
]

for i in range(len(menu)):
    print(f'{i+1}. {menu[i]["name"]} : {menu[i]["price"]}')

product = menuInput()
print(product)
