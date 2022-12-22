# import semua
import persegi

# import secara eksplisit
from persegi_panjang import luas, keliling
from datetime import datetime

print("Tanggal dan waktu sekarang:")
today = datetime.today()
print(today.strftime("%d/%m/%Y %H:%M:%S"), "\n")

print("Luas persegi : ", persegi.luas(5))
print("Luas persegi panjang: ", luas(4, 10))
print("Keliling persegi panjang: ", keliling(20, 10))

print("\nPath modul persegi :")
print(persegi.__file__)
