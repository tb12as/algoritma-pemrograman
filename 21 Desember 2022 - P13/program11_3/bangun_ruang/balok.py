def volume(pj, lb, tg):
    return pj * lb * tg


def luas_permukaan(pj, lb, tg):
    a = 2 * pj * lb
    b = 2 * pj * tg
    c = 2 * lb * tg
    return a + b + c
