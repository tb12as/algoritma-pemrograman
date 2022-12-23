def volume(a, t, tb):
    return 1 / 2 * a * t * tb


def luas_permukaan(a, t, c, tb):  # tb = tinggi bangun
    k = a + t + c
    return k * tb + (a * t)
