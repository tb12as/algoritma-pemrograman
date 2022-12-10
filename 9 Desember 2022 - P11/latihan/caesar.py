import string
letters = list(string.ascii_lowercase)

def caesar(string, shift):
    new_letters = letters[shift % 26:] + letters[0:shift % 26]
    result = ''
    for v in string:
        if v.lower() in letters:
            letter = new_letters[letters.index(v.lower())]
            if v.isupper(): letter = letter.upper()
            result += letter
        else:
            result += v

    return result


def decrypt(string, shift):
    return caesar(string, 26 - shift)

if __name__ == '__main__':
    print(caesar('sERANG kota itu besok', 2))
    print(decrypt('ugtCPi mqvc kvw dguqm',2))


