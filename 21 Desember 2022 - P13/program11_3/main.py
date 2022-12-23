# import biasa
from datetime import datetime
from bangun_datar import persegi

# import dengan alias
import bangun_ruang.kubus as kubus

# import kustom
if datetime.now().minute % 2 == 0:
    from bangun_ruang.limas_segiempat import luas_permukaan
else:
    from bangun_ruang.balok import luas_permukaan

# tanggal hari ini
today = datetime.today()
print(today.strftime("%d/%m/%Y %H:%M:%S"))

# tes persegi
print("\nLuas persegi:", persegi.luas(12))
print("Keliling persegi:", persegi.keliling(12))

# tes kubus
print("\nVolume kubus:", kubus.volume(15))
print("Luas permukaan kubus:", kubus.luas_permukaan(10), '\n')

# tes luas permukaan limas segiempat / balok
module = luas_permukaan.__module__
bangun_ruang = (module.split('.')[1]).replace('_', ' ')
print(f'Luas permukaan {bangun_ruang}:', luas_permukaan(10, 12, 11), '\n')

# path modul kubus
print("Path modul kubus :", kubus.__file__)
