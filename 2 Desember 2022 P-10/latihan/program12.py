r = 1
c = 1
length = 10
while (r <= length):
    while (c <= length):
        print(f'{(c * r):4}', end='')
        c += 1

    r += 1
    c = 1
    print('')
