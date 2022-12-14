def draw():
    for x in range(6):
        for y in range(x + 1):
            print(' *', end='')
        print('')

    r2 = list(range(1, 6))
    r2.reverse()
    for x in r2:
        for y in (range(x)):
            print(' *', end='')
        print('')


draw()
