def draw():
    for x in range(1, 12):
        for y in range(1, 7):
            if x <= 6 and y <= x:
                print(' *', end='')
            elif x > 6 and y <= (x - (x - 6) * 2):
                print(' *', end='')
        print('')


draw()
