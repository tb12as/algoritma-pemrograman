from math import pi


def volume(r, tb):
    return pi * r ** 2 * tb


def luas_permukaan(r, tb):
    l_alas = pi * r ** 2
    l_selimit = 2 * pi * r * tb
    return l_selimit + (2 * l_alas)
