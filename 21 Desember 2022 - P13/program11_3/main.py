from helper.input import float_input
from bangun_datar import persegi
import bangun_datar.segitiga as segitiga
# from luas.persgi import *
# import luas.persegi as persegi


# Tes persegi
sisi = float_input("Masukkan panjang sisi persegi : ")

print("Luas persegi:", persegi.luas(sisi))
print("Keliling persegi:", persegi.keliling(sisi))

print("\n")
# Tes segitiga
alas = float_input("Masukkan panjang alas segitiga : ")
tinggi = float_input("Masukkan tinggi segitiga : ")

s1 = float_input("Masukkan panjang sisi 1  segitiga : ")
s2 = float_input("Masukkan panjang sisi 2  segitiga : ")
s3 = float_input("Masukkan panjang sisi 3  segitiga : ")
print("Luas segitiga: ", segitiga.luas(alas, tinggi))
print("Keliling segitiga: ", segitiga.keliling(s1, s2, s3))


# Todo
# Hapus helper
# Test contoh tes gunakan angka statis ae
