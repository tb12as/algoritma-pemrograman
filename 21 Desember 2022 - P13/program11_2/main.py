# import semua
import tabung

# import secara eksplisit
from kubus import volume, luas_permukaan
from datetime import datetime

print("Tanggal dan waktu sekarang:")
today = datetime.today()
print(today.strftime("%d/%m/%Y %H:%M:%S"))

# tes tabung
print("\nVolume tabung :", tabung.volume(7, 10))
print("Luas Permukaan tabung :", tabung.luas_permukaan(7, 10))

# tes kubus
print("\nVolume kubus :", volume(20))
print("Luas Permukaan kubus :", luas_permukaan(20))

print("\nPath modul tabung :")
print(tabung.__file__)
