from math import sqrt


def volume(pj, lb, tg):
    return 1 / 3 * pj * lb * tg


def luas_permukaan(pj, lb, tg):
    c1 = sqrt((lb / 2) ** 2 + tg ** 2)
    l1 = 1 / 2 * pj * c1  # luas segitiga 1

    c2 = sqrt((pj / 2) ** 2 + tg ** 2)
    l2 = 1 / 2 * lb * c2  # luas segitiga 2

    l3 = pj * lb  # luas persegi panjang

    return ((l1 + l2) * 2) + l3
