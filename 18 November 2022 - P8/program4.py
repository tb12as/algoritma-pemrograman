# https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them

def intInput(message):
    number = input(message)
    if (number.isnumeric()):
        return int(number)
    else:
        print('Input harus berupa angka!')
        return intInput(message)


def duplicateCount(arr):
    seen = set()
    count = 0
    for item in arr:
        if item in seen:
            count += 1
        else:
            seen.add(item)

    return count


# Jumlah sudut segitiga jika ditambah harus 180deg, but who cares anyway?
a = intInput("Masukkan besar sudut A : ")
b = intInput("Masukkan besar sudut B : ")
c = intInput("Masukkan besar sudut C : ")
sama = duplicateCount([a, b, c])

if (sama == 2):
    jenis = 'sama sisi'
elif (sama == 1):
    jenis = 'sama kaki'
else:
    jenis = 'sembarang'

print(
    f'Segitiga {jenis}, dimana memiliki nilai sudut a={a}, b={b}, dan c={c}')
